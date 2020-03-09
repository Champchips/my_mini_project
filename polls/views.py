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
    # if start_date - current_date < 0:
    poll = Poll.objects.all()
    p = Poll.objects.get(subject="l")
    diff = p.end_date - p.create_date
    seconds_in_day = 24 * 60 * 60
    print(p.end_date)
    print(p.create_date)
    print(divmod(diff.days * seconds_in_day + diff.seconds, 60)[0], divmod(diff.days * seconds_in_day + diff.seconds, 60)[1])
    if request.user.is_authenticated:
        return render(request, 'polls/index.html', { 'poll':poll })
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
