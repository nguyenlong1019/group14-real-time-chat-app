from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from django.utils.safestring import mark_safe
import json


def index(request):
    context = {}
    return render(request, 'chatapp/home.html', context)


def login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # xử lý khi username không tồn tại
        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, "User does not exist!")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password does not exist!!")
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    return redirect('home')
                    

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(request, username=user.username, password=request.POST.get('password1'))
            auth_login(request, authenticated_user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")
    else:
        form = SignupForm()
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='/login/')
def room(request):
    context = {}
    return render(request, 'chatapp/home.html', context)


@login_required(login_url='/login/')
def chat(request, room_name):
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }
    return render(request, 'chatapp/room.html', context)



