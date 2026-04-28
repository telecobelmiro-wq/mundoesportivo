from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Pedido

def home(request):
    produtos = Produto.objects.all()
    valor_final = request.session.pop('total_compra_finalizada', None)
    
    return render(request, 'core/home.html', {
        'produtos': produtos,
        'valor_final': valor_final
    })

def finalizar_compra(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    Pedido.objects.create(produto=produto, quantidade=1)
    return redirect('carrinho')

def carrinho(request):
    itens = Pedido.objects.all()
    total = sum(item.produto.preco * item.quantidade for item in itens)
    return render(request, 'core/carrinho.html', {
        'itens_carrinho': itens,
        'total_carrinho': total
    })

def remover_do_carrinho(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    return redirect('carrinho')

def finalizar_carrinho(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_cliente')
        nome = request.POST.get('Produto')
        itens_no_carrinho = Pedido.objects.all()

        if not itens_no_carrinho.exists():
            return redirect('home')
        
        # for item in itens_no_carrinho: 
        print(itens_no_carrinho.produto.preco)
        print(itens_no_carrinho.quantidade)
        
        total_venda = sum(itens_no_carrinho.produto.preco * itens_no_carrinho.quantidade)
        
        request.session['total_compra_finalizada'] = f"{total_venda:.2f}"

        for item in itens_no_carrinho:
            produto = Produto.Objects.get(itens_no_carrinho.produto)
            produto.estoque -= item.quantidade 
            produto.save()

        Pedido.objects.all().delete()
        
        messages.success(request, f"Compra realizada com sucesso irmão, {nome}!") 
        return redirect('home')