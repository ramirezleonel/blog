from django.shortcuts import render

def bienvenida(request):
    return render(request, 'Inicio/templates/bienvenida.html')

def login(request):
    return render(request, 'Inicio/templates/login.html')