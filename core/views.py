from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Pedido, Categoria

from rest_framework import viewsets
from .models import Produto
from .cereja import ProdutoSerializer, CategoriaSerializer



# 1. LISTAGEM DE PRODUTOS (A que você queria corrigir)
def home(request):
    # Pega as categorias para os botões de filtro
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')
    
    # Filtro base: estoque > 0 e ordenado por preço
    produtos = Produto.objects.filter(estoque__gt=0).order_by("-preco")

    # Se clicou em uma categoria, filtra
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    # Pegamos dados para o contexto (total do carrinho e valor final da última compra)
    valor_final = request.session.pop('total_compra_finalizada', None)
    contagem_carrinho = Pedido.objects.filter(finalizado=False).count()

    context = {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_ativa': categoria_id,
        'valor_final': valor_final,
        'contagem_carrinho': contagem_carrinho
    }
    return render(request, "core/home.html", context)

# 2. DETALHE DO PRODUTO
def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, "core/produto_detail.html", {'produto': produto})

# 3. CARRINHO
def carrinho(request):
    itens = Pedido.objects.filter(finalizado=False)
    total = sum(item.produto.preco * item.quantidade for item in itens)
    return render(request, 'core/carrinho.html', {
        'itens_carrinho': itens,
        'total_carrinho': total
    })

# 4. ADICIONAR AO CARRINHO
def finalizar_compra(request, produto_id): 
    produto = get_object_or_404(Produto, id=produto_id)
    # Verifica se o produto tem estoque antes de criar
    if produto.estoque > 0:
        Pedido.objects.create(produto=produto, quantidade=1, finalizado=False)
    else:
        messages.error(request, "Produto sem estoque!")
    return redirect('carrinho')

# 5. REMOVER DO CARRINHO
def remover_do_carrinho(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()
    return redirect('carrinho')

# 6. FINALIZAR A VENDA (BAIXA NO ESTOQUE)
def finalizar_carrinho(request):
    if request.method == 'POST':
        nome_cliente = request.POST.get('nome_cliente')
        itens = Pedido.objects.filter(finalizado=False)
        total_venda = 0
         
        for item in itens:
            qtd_form = request.POST.get(f'quantidade_{item.id}')
            if qtd_form:
                quantidade = int(qtd_form)
                # Atualiza o pedido
                item.usuario = nome_cliente
                item.quantidade = quantidade
                item.finalizado = True
                item.save()
            
                # Soma o total e tira do estoque do produto
                total_venda += (item.produto.preco * quantidade)
                item.produto.estoque -= quantidade
                item.produto.save()

        request.session['total_compra_finalizada'] = f"{total_venda:.2f}"
        messages.success(request, f"Compra finalizada com sucesso, {nome_cliente}!")
        return redirect('home')
    return redirect('carrinho')

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    # Substituímos o .all() pelo .filter() com o modificador __gt
    queryset = Produto.objects.filter(estoque__gt=0)
    serializer_class = ProdutoSerializer