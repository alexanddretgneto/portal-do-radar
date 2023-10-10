# pesquisa/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pesquisar_produto, name='pesquisar_produto'),
]
