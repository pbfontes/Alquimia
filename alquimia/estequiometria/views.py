from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Pesquisa


def index(request):
    pesquisas_anteriores = Pesquisa.objects.order_by("-data_da_pesquisa")
    contexto = {"pesquisas_anteriores": pesquisas_anteriores}
    return render(request, "estequiometria/index.html", contexto)


def pesquisa_anterior(request, id_pesquisa):
    pesquisa = Pesquisa.objects.get(id=id_pesquisa)
    return HttpResponse(pesquisa)
