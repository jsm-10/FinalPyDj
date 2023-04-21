from django.shortcuts import render
from .models import Opinion

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
    # Obtener todas las opiniones existentes
    opiniones = Opinion.objects.all()
    # Renderizar la página de opiniones con el formulario y las opiniones existentes
    return render(request, 'OPBOoks/index.html', {'opiniones': opiniones})

def editar_opinion(request, id):
    # Obtener la opinión a editar
    opinion = Opinion.objects.get(id=id)
    if request.method == 'POST':
        # Procesar el formulario para guardar la opinión editada
        opinion_editada = request.POST.get('opinion_editada')
        opinion.opinion = opinion_editada
        opinion.save()
        # Redirigir a la página de opiniones
        return redirect('index')
    else:
        # Renderizar la página para editar la opinión
        return render(request, 'OPBOoks/editar_opinion.html', {'opinion': opinion})
