from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.form, name = "form"),
    path("cadastrar/", views.cadastrar_projeto, name = "cadastrar_projeto"),
    path("listar/", views.listar, name = "listar_projeto"),
    path("<int:id>/visualizar/", views.visualizar_projeto, name = "visualizar_projeto"),
    path("<int:id>/equipe/", views.equipe, name = "equipe"),
    path("<int:id>/equipe/atualizar/", views.atualizar_equipe_projeto, name = "atualizar_equipe_projeto"),
    path("<int:id>/editar", views.editar_projetom, name = "editar_projeto"),
    path("<int:id>/inativar", views.inativar_projeto, name = "inativar_projeto"),
]
