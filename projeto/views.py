from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home_page(request):
    return render(request,"home.html")

def login_page(request):
    return render(request,"login.html")

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home_page)
        else:
            messages.error(request, 'Usuario ou senha invalidos')
    return redirect(login_page)

def create_client(request):
    return render(request, "client-form.html")
    


