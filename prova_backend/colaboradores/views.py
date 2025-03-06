from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborador
from .forms import ColaboradorForm

def listar(request):
    colaboradores = Colaborador.objects.all()
    context = {"colaboradores": colaboradores}
    return render(request, "colaboradores/listar.html", context)


def cadastrar(request):
    if request.method == 'POST':
        
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar')  
    else:
        
        form = ColaboradorForm()

    context = {'form': form}
    return render(request, 'colaboradores/cadastrar_colaboradores.html', context)

def editar(request, id_colaborador):
    colaborador = get_object_or_404(Colaborador, id_colaborador = id_colaborador)
    if request.method != 'POST':
        form = ColaboradorForm(instance = colaborador)

    else:
        form = ColaboradorForm(request.POST, instance = colaborador)

        if form.isvalid():
            form.save()
            return redirect('listar')

    context = {'form': form}

    return render(request, 'colaboradores/editar.html', context)

    from django.shortcuts import render, get_object_or_404
from .models import Colaborador

def visualizar(request, id_colaborador):
    colaborador = get_object_or_404(Colaborador, id_colaborador = id_colaborador)  # Busca o colaborador pelo ID
    context = {'colaborador': colaborador}
    return render(request, 'colaboradores/visualizar.html', context)