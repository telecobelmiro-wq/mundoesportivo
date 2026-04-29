from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Pedido

def home(request):
    produtos = Produto.objects.all()
    valor_final = request.session.pop('total_compra_finalizada', None)
    
    contagem_carrinho = Pedido.objects.count()
    
    return render(request, 'core/home.html', {
        'produtos': produtos,
        'valor_final': valor_final,
        'contagem_carrinho': contagem_carrinho 
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
        nome_cliente = request.POST.get('nome_cliente')
        itens = Pedido.objects.all()
        total_venda = 0
        
        for item in itens:

            qtd_form = request.POST.get(f'quantidade_{item.id}')
            
            if qtd_form:
                item.quantidade = int(qtd_form)
                item.save()
            
            total_venda += (item.produto.preco * item.quantidade)
            item.produto.estoque -= item.quantidade
            item.produto.save()

        request.session['total_compra_finalizada'] = f"{total_venda:.2f}"
        itens.delete()
        messages.success(request, f"Compra finalizada com sucesso, {nome_cliente}!")
        return redirect('home')