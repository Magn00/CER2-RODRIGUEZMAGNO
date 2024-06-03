# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Profesor
from .forms import ProyectoForm

def onePage(request):
    tematica = request.GET.get('tematica', None)
    sin_patrocinio = request.GET.get('sin_patrocinio', None)
    proyectos = Proyecto.objects.all()
    
    if request.user.is_authenticated:
        if hasattr(request.user, 'profesor'):
            if tematica:
                proyectos = proyectos.filter(tematica=tematica)
            if sin_patrocinio:
                proyectos = proyectos.filter(profesor__isnull=True)
        elif hasattr(request.user, 'estudiante'):
            proyectos = Proyecto.objects.filter(estudiante=request.user.estudiante)
        else:
            proyectos = Proyecto.objects.filter(patrocinado=True)
    else:
        if tematica:
            proyectos = proyectos.filter(patrocinado=True, tematica=tematica)
        else:
            proyectos = proyectos.filter(patrocinado=True)
    
    return render(request, 'core/onePage.html', {'proyectos': proyectos})

@login_required
def patrocinar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if hasattr(request.user, 'profesor'):
        profesor = Profesor.objects.get(usuario=request.user)
        proyecto.profesor = profesor
        proyecto.patrocinado = True
        proyecto.save()
    return redirect('onePage')

@login_required
def proyectos(request):
    if hasattr(request.user, 'profesor'):
        proyectos = Proyecto.objects.all()
    elif hasattr(request.user, 'estudiante'):
        proyectos = Proyecto.objects.filter(estudiante=request.user.estudiante)
    else:
        proyectos = Proyecto.objects.filter(patrocinado=True)
    return render(request, 'core/onePage.html', {'proyectos': proyectos})

@login_required
def nuevo_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.estudiante = request.user.estudiante
            proyecto.save()
            return redirect('onePage')
    else:
        form = ProyectoForm()
    return render(request, 'core/onePage.html', {'form': form})

@login_required
def modificar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, estudiante=request.user.estudiante)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('onePage')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'core/onePage.html', {'form': form})

