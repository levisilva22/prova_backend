from django.urls import path
from . import views


urlpatterns = [
    path("listar/", views.listar, name="listar"),
    path("cadastrar/", views.cadastrar, name = "cadastrar_colaborador"),
    path("<int:id_colaborador>/editar/", views.editar, name = "editar"),
    path("<int:id_colaborador>/visualizar/", views.visualizar, name = "visualizar"),
]
