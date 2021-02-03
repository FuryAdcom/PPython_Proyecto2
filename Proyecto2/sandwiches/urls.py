from django.urls import path

from . import views

#definicion de rutas para las vistas
urlpatterns = [

    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('extras/', views.extra, name='extras')

]