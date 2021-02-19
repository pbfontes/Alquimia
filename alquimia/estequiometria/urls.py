from django.urls import path

from . import views

app_name = "estequiometria"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "<int:id_pesquisa>/visualizar/",
        views.pesquisa_anterior,
        # o valor 'name' é chamado pela template tag {% url %}
        name="pesquisa_anterior",
    ),
    path("pesquisar/", views.pesquisar, name="pesquisar"),
]