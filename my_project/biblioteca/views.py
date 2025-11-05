from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, "biblioteca/livro_list.html", {"livros": livros})

def cria_livro(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_livros")
    return render(request, "biblioteca/livro_form.html", {"form": form})

def edita_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect("lista_livros")
    return render(request, "biblioteca/livro_form.html", {"form": form})

def deleta_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        return redirect("lista_livros")
    return render(request, "biblioteca/livro_confirm_delete.html", {"livro": livro})
