from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("info/", views.info),
    path("index/", views.index, name='index'),
    path("index/condicionais", views.condicionais),
    path("produtos", views.produtos),
    path("contato/<str:telefone>/", views.contato, name='contato'),
    path('about/', views.about, name='about'),
    path('base/', views.about, name='base'),

    
]