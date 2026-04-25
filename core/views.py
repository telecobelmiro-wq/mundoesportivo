from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Pedido

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'core/home.html', {'produtos': produtos})

def finalizar_compra(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    Pedido.objects.create(produto=produto)
    return redirect('carrinho')

def carrinho(request):
    itens = Pedido.objects.all()
    total = sum(item.produto.preco for item in itens)
    return render(request, 'core/carrinho.html', {
        'itens_carrinho': itens,
        'total_carrinho': total
    })

def remover_do_carrinho(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    return redirect('carrinho')