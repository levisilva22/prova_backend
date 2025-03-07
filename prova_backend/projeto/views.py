from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .forms import ProjetoForm
from .models import Projeto
from colaboradores.models import Colaborador
import json

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
    projetos = Projeto.objects.all()
    context = {"projetos": projetos}
    return render(request, "projeto/listar.html", context)

@csrf_exempt
def cadastrar_projeto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            projeto = Projeto.objects.create(
                projeto=data['projeto'],
                id_financiador_id=data['id_financiador'],
                id_area_tecnologica_id=data['id_area_tecnologica'],
                coordenador=data['coordenador'],
                ativo=data['ativo'],
                inicio_vigencia=data['inicio_vigencia'],
                fim_vigencia=data['fim_vigencia'],
                valor=data['valor'],
                qnt_membros=data['qnt_membros'],
                equipe_id=data['equipe']
            )
            return JsonResponse({
                'id_projeto': projeto.id_projeto,
                'projeto': projeto.projeto,
                'id_financiador': projeto.id_financiador.id,
                'id_area_tecnologica': projeto.id_area_tecnologica.id,
                'coordenador': projeto.coordenador,
                'ativo': projeto.ativo,
                'inicio_vigencia': projeto.inicio_vigencia.strftime('%Y-%m-%d'),
                'fim_vigencia': projeto.fim_vigencia.strftime('%Y-%m-%d'),
                'valor': float(projeto.valor),
                'qnt_membros': projeto.qnt_membros,
                'equipe': projeto.equipe.id
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def visualizar_projeto(request, id_projeto):
    projeto = get_object_or_404(Projeto, id_projeto=id_projeto)
    return JsonResponse({
        'id_projeto': projeto.id_projeto,
        'projeto': projeto.projeto,
        'id_financiador': projeto.id_financiador.id,
        'id_area_tecnologica': projeto.id_area_tecnologica.id,
        'coordenador': projeto.coordenador,
        'ativo': projeto.ativo,
        'inicio_vigencia': projeto.inicio_vigencia.strftime('%Y-%m-%d'),
        'fim_vigencia': projeto.fim_vigencia.strftime('%Y-%m-%d'),
        'valor': float(projeto.valor),
        'qnt_membros': projeto.qnt_membros,
        'equipe': projeto.equipe.id
    })

@csrf_exempt
def editar_projeto(request, id_projeto):
    if request.method == 'PATCH':
        projeto = get_object_or_404(Projeto, id_projeto=id_projeto)
        try:
            data = json.loads(request.body)
            if 'projeto' in data:
                projeto.projeto = data['projeto']
            if 'id_financiador' in data:
                projeto.id_financiador_id = data['id_financiador']
            if 'id_area_tecnologica' in data:
                projeto.id_area_tecnologica_id = data['id_area_tecnologica']
            if 'coordenador' in data:
                projeto.coordenador = data['coordenador']
            if 'ativo' in data:
                projeto.ativo = data['ativo']
            if 'inicio_vigencia' in data:
                projeto.inicio_vigencia = data['inicio_vigencia']
            if 'fim_vigencia' in data:
                projeto.fim_vigencia = data['fim_vigencia']
            if 'valor' in data:
                projeto.valor = data['valor']
            if 'qnt_membros' in data:
                projeto.qnt_membros = data['qnt_membros']
            if 'equipe' in data:
                projeto.equipe_id = data['equipe']
            projeto.save()
            return JsonResponse({
                'id_projeto': projeto.id_projeto,
                'projeto': projeto.projeto,
                'id_financiador': projeto.id_financiador.id,
                'id_area_tecnologica': projeto.id_area_tecnologica.id,
                'coordenador': projeto.coordenador,
                'ativo': projeto.ativo,
                'inicio_vigencia': projeto.inicio_vigencia.strftime('%Y-%m-%d'),
                'fim_vigencia': projeto.fim_vigencia.strftime('%Y-%m-%d'),
                'valor': float(projeto.valor),
                'qnt_membros': projeto.qnt_membros,
                'equipe': projeto.equipe.id
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def inativar_projeto(request, id_projeto):
    if request.method == 'POST':
        projeto = get_object_or_404(Projeto, id_projeto=id_projeto)
        projeto.ativo = False
        projeto.save()
        return JsonResponse({'status': 'Projeto inativado com sucesso'})
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def equipe(request):
    equipes = Colaborador.objects.all()
    context = {'equipes': equipes}
    return render(request, 'projeto/listar_todas_equipes.html', context)

@csrf_exempt
def atualizar_equipe_projeto(request, id_projeto):
    if request.method == 'POST':
        try:
            projeto = get_object_or_404(Projeto, id_projeto=id_projeto)
            data = json.loads(request.body)
            
            
            if 'equipe_id' in data:
                equipe = get_object_or_404(Colaborador, id=data['equipe_id'])
                projeto.equipe = equipe
                projeto.save()
                
                return JsonResponse({
                    'status': 'Equipe atualizada com sucesso',
                    'equipe_id': equipe.id,
                    'equipe_nome': equipe.nome
                }, status=200)
            
            return JsonResponse({'error': 'Nenhuma equipe foi enviada'}, status=400)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)
