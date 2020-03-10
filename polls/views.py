import datetime
from urllib import response

from astroid.scoped_nodes import objects
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request

from polls.forms import PollForm
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
        diff_end_date =  new_end_date - datetime.datetime.now()
        diff_start_date =  new_start_date - datetime.datetime.now()
        result_end_date = divmod(diff_end_date.days * seconds_in_day + diff_end_date.seconds, 60)[0]
        result_start_date = divmod(diff_start_date.days * seconds_in_day + diff_start_date.seconds, 60)[0]
        if result_start_date > 0:
            single_poll.duration = 0
        elif result_start_date < 0 and result_end_date > 0:
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
            newpoll = Poll(subject = request.POST['subject'], 
            picture = request.FILES['picture'], detail = request.POST['detail'], password = request.POST['password'], 
            create_by = User.objects.get(pk=request.user.id), start_date = request.POST['start_date'], 
            end_date = request.POST['end_date'], create_date = datetime.datetime.now())
            newpoll.save()
            return redirect('index')
    else:
        form = PollForm()
    # if request.user.is_authenticated:
    return render(request, 'polls/create.html', {'form': form })
    # else:
    #     return redirect('login')
@login_required
def poll_detail(request):
    return HttpResponse('Your Poll Detail!')
@login_required
def poll_update(request):
    return HttpResponse('Update your Poll')
@login_required
def poll_views(request):
    poll_item = request.POST.get("poll_item.id"," ")
    poll = Poll.objects.get(pk=poll_item)

    return render(request, 'polls/view.html', {'poll': poll })
