from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Pesquisa(models.Model):
    reagentes_reacao = models.CharField(max_length=30)
    produtos_reacao = models.CharField(max_length=30)
    data_da_pesquisa = models.DateTimeField("data da pesquisa", default=timezone.now)

    def __str__(self):
        nome = f"{self.reagentes_reacao} -> {self.produtos_reacao}"
        return nome

    def pesquisado_recentemente(self):
        # a pesquisa ocorreu ha menos de 3 dias?
        return self.data_da_pesquisa >= timezone.now() - timedelta(days=3)


class TabelaPeriodica(models.Model):
    atomic_number = models.IntegerField()
    symbol = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    atomic_mass = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.name
