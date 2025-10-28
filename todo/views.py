from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Task

def home_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('task_list')
    return render(request, 'todo/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
    return render(request, 'todo/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def task_list_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(user=request.user, title=title)
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/home.html', {'tasks': tasks})
