from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Pesquisa


def index(request):
    return HttpResponse("index da estequiometria")


def pesquisa_anterior(request, id_pesquisa):
    pesquisa = Pesquisa.objects.get(id=id_pesquisa)
    return HttpResponse(pesquisa)
