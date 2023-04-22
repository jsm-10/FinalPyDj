from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import Opinion

class IndexView(View):
    def get(self, request):
        opiniones = Opinion.objects.all()
        return render(request, 'OPBOoks/index.html', {'opiniones': opiniones})

    def post(self, request):
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        libro = request.POST.get('libro')
        opinion = request.POST.get('opinion')
        nueva_opinion = Opinion(nombre=nombre, apellido=apellido, libro=libro, opinion=opinion)
        nueva_opinion.save()
        return redirect('index')

    def delete(self, request):
        id_opinion = request.POST.get('id_opinion')
        Opinion.objects.get(id=id_opinion).delete()
        return redirect('index')

class BusquedaView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        opiniones = Opinion.objects.filter(Q(libro__icontains=query))
        return render(request, 'OPBOoks/busqueda.html', {'opiniones': opiniones})

class EliminarOpinionView(View):
    def get(self, request, id):
        opinion = Opinion.objects.get(id=id)
        return render(request, 'OPBOoks/eliminar_opinion.html', {'opinion': opinion})

    def post(self, request, id):
        opinion = Opinion.objects.get(id=id)
        opinion.delete()
        return redirect('index')

class EditarOpinionView(View):
    def get(self, request, id):
        opinion = Opinion.objects.get(id=id)
        return render(request, 'OPBOoks/editar_opinion.html', {'opinion': opinion})

    def post(self, request, id):
        opinion = Opinion.objects.get(id=id)
        opinion_editada = request.POST.get('opinion_editada')
        opinion.opinion = opinion_editada
        opinion.save()
        return redirect('index')
