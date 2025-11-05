from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros/novo/', views.cria_livro, name='cria_livro'),
    path('livros/editar/<int:pk>/', views.edita_livro, name='edita_livro'),
    path('livros/deletar/<int:pk>/', views.deleta_livro, name='deleta_livro'),
]
