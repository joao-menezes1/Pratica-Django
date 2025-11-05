from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def hello(request):
    return HttpResponse("hello, João Vittor")

def info(request):
    data =   {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  }
    return JsonResponse(data)

def index(request):
    contexto = {"nome": "João Vittor",
                "numero": 4,
                "resultado": 4*2}
    return render(request, "blog/index.html", contexto)

def condicionais(request):
    context = {
        "is_logged_in": True,
        "idade": 18
    }
    return render(request, "blog/index.html", context)

def produtos(request):
    lista_produtos = [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Mouse", "preco": 100},
        {"nome": "Teclado", "preco": 200},
    ]
    context = {"produtos": lista_produtos}
    return render(request, "blog/produtos.html", context)

def contato(request, telefone):
    context = {"telefone": telefone}
    return render(request, "blog/contato.html", context)


def about(request):
    return render(request, "blog/about.html")

