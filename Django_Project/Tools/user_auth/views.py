from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import user_form
from .forms import RegisterUserForm
# Create your views here.


def user_login(request):
    form = user_form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("There was an error! login again."))
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        return render(request, "user_auth/index.html", {'form': form})
    

def user_logout(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('home')

def user_register(request):
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successfully!"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request,'user_auth/user_register.html', {'form':form})