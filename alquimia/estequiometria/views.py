from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pesquisa
from django.urls import reverse

# Create your views here.


def index(request):
    pesquisas_anteriores = Pesquisa.objects.order_by("-data_da_pesquisa")
    contexto = {
        "pesquisas_anteriores": pesquisas_anteriores
    }  # relaciona as variaveis do template com os objetos pythons aqui do views
    return render(request, "estequiometria/index.html", contexto)


def pesquisa_anterior(request, id_pesquisa):
    pesquisa = Pesquisa.objects.get(id=id_pesquisa)
    return HttpResponse(pesquisa)


def pesquisar(request):
    # validar se os heagentes e produtos digitados são validos
    # capturar as informações e executar as contas
    # redirecionar para a página de resultado
    # lá teremos a opção de salvar a pesquisa
    print(request.POST["reagentes"])
    print(request.POST["produtos"])
    return HttpResponseRedirect(reverse("estequiometria:index"))  # reverse é necessário
