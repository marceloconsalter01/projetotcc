from django.shortcuts import render, HttpResponse

def paginaInicial(request):
    descricao = "pega na minha pica2"
    return render(request,"login.html")