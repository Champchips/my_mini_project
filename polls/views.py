from builtins import object
from urllib import response
from astroid.scoped_nodes import objects
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.contrib.auth.models import User
from polls.forms import PollForm
from polls.models import Poll, Poll_Choice, Poll_Vote


# Create your views here.
def index(request):
    context = {}
    poll = Poll.objects.all()
    context = {
        'poll':poll
    }
    if request.user.is_authenticated:
        return render(request, 'polls/index.html', context=context)
    else:
        return redirect('login')
def poll_create(request):
    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES)
        if form.is_valid():
            newpoll = Poll(subject = request.POST['subject'], 
            picture = request.FILES['picture'], detail = request.POST['detail'], password = request.POST['password'], 
            create_by = User.objects.get(pk=request.user.id))
            newpoll.save()
            return redirect('index')
    else:
        form = PollForm()
    if request.user.is_authenticated:
        return render(request, 'polls/create.html', {'form': form })
    else:
        return redirect('login')
def poll_detail(request):
    return HttpResponse('Your Poll Detail!')
def poll_update(request):
    return HttpResponse('Update your Poll')
