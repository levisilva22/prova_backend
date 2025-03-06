from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ProjetoForm
from .models import Projeto


def form(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("form")
    else:
        form = ProjetoForm()

    context = {"form": form}
    return render(request, "projeto_form.html", context)


def listar(request):
    listar = Projeto.objects.all()
    context = {"listar": listar}

    return render(request, "projeto/listar.html", context)


def cadastrar_projeto(request):
    if request.method == "POST":
        form_projeto = ProjetoForm(request.POST)
        if form_projeto.is_valid():
            form_projeto = form_projeto.save()
            return redirect("listar_projeto")
    else:
        form_projeto = ProjetoForm()

    context = {"form_projeto": form_projeto}
    return render(request, "projeto/cadastrar.html", context)
