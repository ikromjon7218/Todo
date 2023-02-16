from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
def todo(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get('status') == 'on': qiymat = True
            else: qiymat = False
            Todo.objects.create(
                title=request.POST.get("title"),
                time=request.POST.get("time"),
                description=request.POST.get("d"),
                status=qiymat,
                foydalanuvchi=request.user)
            return redirect("/todo/")
        data = {"Todo": Todo.objects.filter(foydalanuvchi=request.user)}
        return render(request, "todo.html", data)
    return redirect('/')


def todo_edit(request, son):
    if request.method == "POST":
        if Todo.objects.get(id=son).foydalanuvchi == request.user:
            if request.POST.get('status') == 'on':     qiymat = True
            else:      qiymat = False
            Todo.objects.filter(id=son).update(
            title=request.POST.get("title"),
            time = request.POST.get("time"),
            description = request.POST.get("description"),
            status = qiymat)
        return redirect('/todo/')
    data = {"todo": Todo.objects.get(id=son)}
    return render(request, "todo_edit.html", data)
def todo_delete(request, son):
    if Todo.objects.get(id=son).foydalanuvchi == request.user:
        Todo.objects.get(id=son).delete()
    return redirect('/todo/')
def loginview(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('l'), password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/todo/')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST" and request.POST.get('p') == request.POST.get('cp'):
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p'), )
        return redirect('/')
    return render(request, 'register.html')