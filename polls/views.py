import datetime
from builtins import object
from urllib import response

from astroid.scoped_nodes import objects
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.api import success
from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request

from polls.forms import ChoiceForm, PollForm
from polls.models import Poll, Poll_Choice, Poll_Vote


# Create your views here.
@login_required
def index(request):
    context = {}
    poll = Poll.objects.all()
    for single_poll in poll:
        new_end_date = single_poll.end_date.replace(tzinfo=None)
        new_start_date = single_poll.start_date.replace(tzinfo=None)
        seconds_in_day = 24 * 60 * 60
        diff_end_date = new_end_date - datetime.datetime.now()
        diff_start_date = new_start_date - datetime.datetime.now()
        result_end_date = divmod(diff_end_date.days * seconds_in_day + diff_end_date.seconds, 60)[0]
        result_start_date = divmod(diff_start_date.days * seconds_in_day + diff_start_date.seconds, 60)[0]
        if result_start_date > 0:
            single_poll.duration = 0
        elif result_start_date < 0 and result_end_date >= 0:
            single_poll.duration = result_end_date
        elif result_end_date < 0:
            single_poll.duration = 0
        single_poll.save()
    context['poll'] = poll
    if request.user.is_authenticated:
        return render(request, 'polls/index.html', context=context)
    else:
        return redirect('login')


@login_required
def poll_create(request):
    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES)
        if form.is_valid():
            newpoll = Poll(subject=request.POST['subject'],
                           picture=request.FILES['picture'], detail=request.POST['detail'], password=request.POST['password'],
                           create_by=User.objects.get(pk=request.user.id), start_date=request.POST['start_date'],
                           end_date=request.POST['end_date'], create_date=datetime.datetime.now())
            newpoll.save()
            return redirect('index')
    else:
        form = PollForm()
    # if request.user.is_authenticated:
    return render(request, 'polls/create.html', {'form': form})
    # else:
    #     return redirect('login')
@login_required
def my_poll(request):
    context = {}
    p = Poll.objects.all()
    user = request.user.id
    context['p'] = p
    context['user'] = user
    return render(request, 'polls/mypoll.html', context=context)


@login_required
def poll_choice_update(request, poll_id):
    if ('edit' in request.POST):
        poll = Poll.objects.get(pk=poll_id)
        choice = Poll_Choice.objects.all
        return render(request, 'polls/edit.html', {'poll':poll, 'choice':choice})
    if ('delete' in request.POST):
        p = Poll.objects.get(pk=poll_id)
        p.delete()
        return redirect('my_poll')


@login_required
def poll_views(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    vote = Poll_Vote.objects.all
    choice = Poll_Choice.objects.all
    return render(request, 'polls/view.html', {'poll': poll, 'vote': vote, 'choice' : choice})


@login_required
def poll_detail(request):
    return HttpResponse('Detail')

@login_required
def add_choice(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.user.id != poll.create_by.id:
        return redirect('/')
    if request.method == "POST":
        form = ChoiceForm(request.POST, request.FILES)
        if form.is_valid():
            new_choice = form.save(commit=False)
            new_choice.poll_id_id = poll_id
            new_choice.save()
            return redirect('my_poll')
    else:
        form = ChoiceForm()
    return render(request,'polls/add_choice.html', {'form':form})
@login_required
def delete_choice(request, choice_id):
    if request.method == "POST":
        ch = Poll_Choice(pk=choice_id)
        ch.delete()
        return redirect('my_poll')
def poll_update(request, poll_id):
    if request.method == 'POST':
        update_poll = Poll.objects.get(pk=poll_id)
        update_poll.subject = request.POST['subject']
        update_poll.detail = request.POST['detail']
        update_poll.picture = request.FILES['picture']
        update_poll.password = request.POST['password']
        update_poll.start_date = request.POST['start_date']
        update_poll.end_date = request.POST['end_date']
        update_poll.save()
    return redirect('my_poll')
def poll_vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    choice = Poll_Choice.objects.all
    return render(request, 'polls/vote.html', {'poll': poll, 'choice':choice})
def vote_poll(request, poll_id, choice_id):
    if request.method == "POST":
        vote_by = User.objects.get(pk=request.user.id)
        poll = Poll.objects.get(pk=poll_id)
        choice = Poll_Choice.objects.get(pk=choice_id)
        que = Poll_Vote.objects.filter(vote_by_id=vote_by.id, poll_id_id = poll.id)
        if not(que):
            n_vote = Poll_Vote(poll_id = poll, choice_id = choice, vote_by=vote_by)
            n_vote.save()
    return redirect('index')
