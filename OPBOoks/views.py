from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import Opinion
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, NuevaOpinionForm


class IndexView(View):
    def get(self, request):
        opiniones = Opinion.objects.all()
        form = NuevaOpinionForm(user=request.user)
        return render(request, 'OPBooks/index.html', {'opiniones': opiniones, 'form': form})

    def post(self, request):
        form = NuevaOpinionForm(request.POST, user=request.user)

        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            libro = form.cleaned_data.get('libro')
            opinion = form.cleaned_data.get('opinion')
            nueva_opinion = Opinion(nombre=nombre, apellido=apellido, libro=libro, opinion=opinion)
            nueva_opinion.save()
            return redirect('index')

        opiniones = Opinion.objects.all()
        return render(request, 'OPBooks/index.html', {'opiniones': opiniones, 'form': form})
    
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
    def get(self, request, pk):
        opinion = Opinion.objects.get(id=pk)
        return render(request, 'OPBOoks/eliminar_opinion.html', {'opinion': opinion})

    def post(self, request, pk):
        opinion = Opinion.objects.get(id=pk)
        opinion.delete()
        return redirect('index')


class EditarOpinionView(View):
    def get(self, request, id):
        opinion = Opinion.objects.get(id=id)
        form = NuevaOpinionForm(instance=opinion, user=request.user)
        return render(request, 'OPBOoks/editar_opinion.html', {'form': form})

    def post(self, request, id):
        opinion = Opinion.objects.get(id=id)
        form = NuevaOpinionForm(request.POST, instance=opinion, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'OPBOoks/editar_opinion.html', {'form': form})

    
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'El nombre de usuario o la contraseña no son válidos')
            return render(request, 'OPBOoks/login.html')
    else:
        return render(request, 'OPBOoks/login.html')
def logout_request(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La cuenta ha sido creada exitosamente.')
            return redirect('login')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f'{field.label}: {error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})