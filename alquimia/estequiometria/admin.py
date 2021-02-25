from django.contrib import admin

# Register your models here.
from .models import Pesquisa, TabelaPeriodica

admin.site.register(Pesquisa)
admin.site.register(TabelaPeriodica)