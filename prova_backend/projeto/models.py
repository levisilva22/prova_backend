from django.db import models
from financiadores.models import Financiador
from areastecnologicas.models import AreasTecnologicas
from colaboradores.models import Colaborador


class Projeto(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100)
    id_financiador = models.ForeignKey(Financiador, on_delete=models.CASCADE)
    id_area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.CASCADE)
    coordenador = models.CharField(max_length=100)
    ativo = models.CharField(max_length=1)
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    qnt_membros = models.IntegerField()
    equipe = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

    def __strs__(self):
        return self.projeto
