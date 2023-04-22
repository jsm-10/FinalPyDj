from django.shortcuts import render, redirect
from .models import Opinion
from django.db.models import Q

def index(request):
    if request.method == 'POST':
        # Procesar el formulario para agregar la opinión
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        libro = request.POST.get('libro')
        opinion = request.POST.get('opinion')
        # Guardar la opinión en la base de datos
        nueva_opinion = Opinion(nombre=nombre, apellido=apellido, libro=libro, opinion=opinion)
        nueva_opinion.save()
    elif request.method == 'DELETE':
        # Eliminar la opinión correspondiente
        id_opinion = request.POST.get('id_opinion')
        Opinion.objects.get(id=id_opinion).delete()
    # Obtener todas las opiniones existentes
    opiniones = Opinion.objects.all()
    # Renderizar la página de opiniones con el formulario y las opiniones existentes
    return render(request, 'OPBOoks/index.html', {'opiniones': opiniones})

def busqueda(request):
    if 'q' in request.GET:
        query = request.GET['q']
        opiniones = Opinion.objects.filter(libro__icontains=query)
    else:
        opiniones = Opinion.objects.all()
    return render(request, 'OPBOoks/busqueda.html', {'opiniones': opiniones})

def eliminar_opinion(request, id):
    opinion = Opinion.objects.get(id=id)
    if request.method == 'POST':
        opinion.delete()
        return redirect('index')
    else:
        return render(request, 'OPBOoks/eliminar_opinion.html', {'opinion': opinion})
    
def editar_opinion(request, id):
    opinion = Opinion.objects.get(id=id)
    if request.method == 'POST':
        opinion_editada = request.POST.get('opinion_editada')
        opinion.opinion = opinion_editada
        opinion.save()
        return redirect('index')
    else:
        return render(request, 'OPBOoks/editar_opinion.html', {'opinion': opinion})
    
    
    
    
