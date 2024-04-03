from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout


def login(request):
    context = {}
    if request.method == 'POST':       
        username = request.POST.get('usuario')
        password = request.POST.get('senha')

        user = authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            return redirect('anexo')
        else:
            #TODO fazer erro de credenciais
            context['erro_login'] = True

    return render(request, 'login/login.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email_parceiro = request.POST.get('email_parceiro')
        integrador = request.POST.get('integrador')


    return render(request, 'cadastro/cadastro.html')


def anexo(request):
    return render(request, 'anexo/anexo.html')