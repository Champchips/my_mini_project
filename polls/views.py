from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.
def index(request):
    return render(request, 'polls/index.html')
def  poll_create(request):
    return HttpResponse('Let Create Your Poll')
def poll_detail(request):
    return HttpResponse('Your Poll Detail!')
def poll_update(request):
    return HttpResponse('Update your Poll')
