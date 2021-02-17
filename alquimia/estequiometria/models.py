from django.db import models
from django.utils import timezone

# Create your models here.
class Pesquisa(models.Model):
    reagentes_reacao = models.CharField(max_length=30)
    produtos_reacao = models.CharField(max_length=30)
    data_da_pesquisa = models.DateTimeField("data da pesquisa", default=timezone.now)
