from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from authen.forms import RegisterForm
# Create your views here.

def my_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong Username or Password'
    return render(request, "authen/login.html", context=context)
def my_register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
           return render(response, "authen/register.html", {"form":form})
    else:
        form = RegisterForm()
    return render(response, "authen/register.html", {"form":form})
def my_logout(request):
    logout(request)
    return redirect('login')