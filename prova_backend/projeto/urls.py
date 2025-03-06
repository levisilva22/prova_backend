from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.form, name = "form"),
    path("cadastrar/", views.cadastrar_projeto, name = "cadastrar_projeto"),
    path("listar/", views.listar, name = "listar_projeto"),
]
