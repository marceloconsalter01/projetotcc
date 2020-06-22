import json
from contextvars import Context
from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from pymongo import MongoClient

from projeto.NaiveBayies import nbml
from projeto.models import db, InsertMongo, FindMongoAll, FindMongoOne, UpdateMongo, DeleteClient_One


def home_page(request):
    return render(request, "home.html")


def list_page(request):
    consulta = FindMongoAll()
    return render(request, "list-form.html", {"consulta": consulta})


def login_page(request):
    return render(request, "login.html")


def edit_page(request):
    return render(request, "client-edit.html")


def redirect_page(request):
    return render(request, "redirect-form.html")


def create_clients(request):
    teste = db.cadastro.find()
    t = get_template('client-form.html')
    #   return HttpResponse(t.render(Context()))
    return render(request, "client-form.html", {"teste": teste})  # ---> importante


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_page)
        else:
            messages.error(request, 'Usuario ou senha invalidos')
    return redirect(login_page)


@csrf_protect
def insert_client(request):
    selecao_nome = request.POST.get('selecao_nome')
    selecao_cpf = request.POST.get('selecao_cpf')
    selecao_email = request.POST.get('selecao_email')
    selecao_1 = request.POST.get('selecao_1')
    selecao_2 = request.POST.get('selecao_2')
    selecao_3 = request.POST.get('selecao_3')
    selecao_4 = request.POST.get('selecao_4')
    selecao_5 = request.POST.get('selecao_5')
    selecao_6 = request.POST.get('selecao_6')
    selecao_7 = request.POST.get('selecao_7')
    selecao_8 = request.POST.get('selecao_8')
    selecao_9 = request.POST.get('selecao_9')
    selecao_10 = request.POST.get('selecao_10')
    selecao_11 = request.POST.get('selecao_11')
    selecao_12 = request.POST.get('selecao_12')
    selecao_13 = request.POST.get('selecao_13')
    selecao_14 = request.POST.get('selecao_14')
    selecao_15 = request.POST.get('selecao_15')
    selecao_16 = request.POST.get('selecao_16')
    selecao_17 = request.POST.get('selecao_17')
    selecao_18 = request.POST.get('selecao_18')
    selecao_19 = request.POST.get('selecao_19')
    selecao_20 = request.POST.get('selecao_20')

    status = InsertMongo(selecao_nome, selecao_cpf, selecao_email, selecao_1,
                selecao_2, selecao_3, selecao_4, selecao_5, selecao_6, selecao_7, selecao_8, selecao_9, selecao_10,
                selecao_11, selecao_12, selecao_13, selecao_14, selecao_15, selecao_16, selecao_17, selecao_18,
                selecao_19, selecao_20)

    if status == True:
        nbml(FindMongoOne(selecao_cpf))
        const = 'Cadastrado com sucesso!'
    elif status == False:
        const = 'CPF já Cadastrado!'

    return render(request, 'client-form.html', {"const": const})


@csrf_protect
def ConsultClient(request):
    cpf = request.POST.get('consulta_cpf')
    consulta_one = FindMongoOne(cpf)
    if consulta_one == None:
        const1 = 'CPF não encontrado'
        return render(request, "list-form.html", {"const": const1})
    else:
        return render(request, "client-edit.html", {"consulta_one": consulta_one})


@csrf_protect
def EditClient(request):
    selecao_nome = request.POST.get('selecao_nome')
    selecao_cpf = request.POST.get('selecao_cpf')
    selecao_email = request.POST.get('selecao_email')
    selecao_1 = request.POST.get('selecao_1')
    selecao_2 = request.POST.get('selecao_2')
    selecao_3 = request.POST.get('selecao_3')
    selecao_4 = request.POST.get('selecao_4')
    selecao_5 = request.POST.get('selecao_5')
    selecao_6 = request.POST.get('selecao_6')
    selecao_7 = request.POST.get('selecao_7')
    selecao_8 = request.POST.get('selecao_8')
    selecao_9 = request.POST.get('selecao_9')
    selecao_10 = request.POST.get('selecao_10')
    selecao_11 = request.POST.get('selecao_11')
    selecao_12 = request.POST.get('selecao_12')
    selecao_13 = request.POST.get('selecao_13')
    selecao_14 = request.POST.get('selecao_14')
    selecao_15 = request.POST.get('selecao_15')
    selecao_16 = request.POST.get('selecao_16')
    selecao_17 = request.POST.get('selecao_17')
    selecao_18 = request.POST.get('selecao_18')
    selecao_19 = request.POST.get('selecao_19')
    selecao_20 = request.POST.get('selecao_20')

    UpdateMongo(selecao_nome, selecao_cpf, selecao_email, selecao_1,
                selecao_2, selecao_3, selecao_4, selecao_5, selecao_6, selecao_7, selecao_8, selecao_9, selecao_10,
                selecao_11, selecao_12, selecao_13, selecao_14, selecao_15, selecao_16, selecao_17, selecao_18,
                selecao_19, selecao_20)

    print(selecao_email)
    print(selecao_1)

    return redirect(edit_page)


def Deletedb(request):
    cpf_exclude = str(request.POST.get('consulta_cpf'))
    valor = DeleteClient_One(cpf_exclude)
    print(valor)
    return redirect(list_page)


