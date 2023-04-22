"""jsmm42123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from OPBOoks.views import IndexView, BusquedaView, EliminarOpinionView, EditarOpinionView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('busqueda/', BusquedaView.as_view(), name='busqueda'),
    path('eliminar/<int:pk>/', EliminarOpinionView.as_view(), name='eliminar_opinion'),
    path('editar/<int:pk>/', EditarOpinionView.as_view(), name='editar_opinion'),
]
