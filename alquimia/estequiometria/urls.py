from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "<int:id_pesquisa>/visualizar/",
        views.pesquisa_anterior,
        name="pesquisa_anterior",
    ),
]