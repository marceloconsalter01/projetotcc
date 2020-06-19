import json
from contextvars import Context

from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from pymongo import MongoClient

from projeto.models import db


def home_page(request):
    return render(request,"home.html")

def login_page(request):
    return render(request,"login.html")

def create_clients(request):
    teste = db.cadastro.find()
    t = get_template('client-form.html')
#   return HttpResponse(t.render(Context()))
    return render(request,"client-form.html",{"teste": teste})   #---> importante

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



@csrf_protect
def insert_client(request):
    data = request.POST.get('selecao_1')
    print(data)
    return render(request, login_page)

    


