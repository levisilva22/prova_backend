from django.db import models


class AreasTecnologicas(models.Model):

    id_area_tecnologica = models.AutoField(primary_key=True)
    area_tecnologia = models.CharField(max_length=100)

    def __str__(self):
        return self.area_tecnologia
