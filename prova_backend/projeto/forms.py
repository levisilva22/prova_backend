from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"
        exclude = [
            "id_projeto"
        ]  
        labels = {
            "projeto": "Nome do Projeto",
            "id_financiador": "Financiador",
            "id_area_tecnologica": "Área Tecnológica",
            "coordenador": "Coordenador",
            "ativo": "Status do Projeto",
            "inicio_vigencia": "Início da Vigência",
            "fim_vigencia": "Fim da Vigência",
            "valor": "Valor do Projeto",
            "qnt_membros": "Quantidade de Membros",
            "equipe": "Equipe Responsável",
        }
        widgets = {
            "inicio_vigencia": forms.DateInput(attrs={"type": "date"}),
            "fim_vigencia": forms.DateInput(attrs={"type": "date"}),
        }
