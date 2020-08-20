from .models import Produtos
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormProduto


def lista_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def novo_produto(request):
    form = FormProduto(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'produto_formulario.html', {'form': form})

def atualiza_produto(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    form = FormProduto(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'produto_formulario.html', {'form': form})

def deleta_produto(request, id):
    produto = get_object_or_404(Produtos, pk=id)

    if request.method == 'POST':
        produto.delete()
        return redirect(lista_produtos)

    return render(request, 'excluir_produto.html', {'produto': produto})


