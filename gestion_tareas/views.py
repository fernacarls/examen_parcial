from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from dateutil.parser import parse
from gestion_tareas.models import tareas, usuarios

# Create your views here.

def ingresar(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        usuario_registrado = 0.
        usuarios_totales = usuarios.objects.all()
        
        for usuario in usuarios_totales:
            if usuario.nombre == nombreUsuario and usuario.psw_usuario == passwordUsuario:
                usuario_registrado = 1
        
        if usuario_registrado == 1:
            return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
        
        else:
            return render(request,'gestion_tareas/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
            })
    return render(request, 'gestion_tareas/ingresar.html')

def dashboard(request):
    tareas_totales = tareas.objects.all()
    return render(request,'gestion_tareas/dashboard.html',{
        'objtarea':tareas_totales,
    })