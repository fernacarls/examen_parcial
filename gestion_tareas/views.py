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
    tareas_usuario = []
    tareas_usuarios = tareas.objects.filter(usuario_responsable='1')
    for ttareas in tareas_usuarios:
        tareas_usuario.append(ttareas)
    
    return render(request,'gestion_tareas/dashboard.html',{
        'objtarea':tareas_usuario,
    })

def nuevoTarea(request):
    if request.method == 'POST':
        tarea_fecha_creacion = request.POST.get('tarea_fecha_creacion')
        tarea_fecha_entrega = request.POST.get('tarea_fecha_entrega')
        tarea_descripcion = request.POST.get('tarea_descripcion')
        tarea_usuario_responsable = request.POST.get('tarea_usuario_responsable')
        tarea_estado_tarea = request.POST.get('tarea_estado_tarea')
        tareas(fecha_creacion=tarea_fecha_creacion, fecha_entrega=tarea_fecha_entrega, descripcion=tarea_descripcion, usuario_responsable=tarea_usuario_responsable, estado_tarea=tarea_estado_tarea).save()
    return render(request, 'gestion_tareas/nuevoTarea.html',{
        'tareas_registradas':tareas.objects.all(),
    })