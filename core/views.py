from django.shortcuts import render

# Create your views here.
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'core/home.html', {'produtos': produtos})

def carrinho(request):
    return render(request, 'core/carrinho.html')