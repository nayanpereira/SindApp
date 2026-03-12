from django.shortcuts import render

def index(request):
    return render(request, 'associado/index.html')

def perfil(request):
    return render(request, 'associado/perfil.html')

def beneficios(request):
    return render(request, 'associado/beneficios.html')

def carteirinha(request):
    return render(request, 'associado/carteirinha.html')