from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self): return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    imagem_url = models.CharField(max_length=200, blank=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self): return self.imagem_url
    estoque = models.IntegerField(default=0)

class Pedido(models.Model):
    usuario = models.CharField(max_length=100, null=True, blank=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_compra = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(default=1)
    finalizado = models.BooleanField(default=False)
    nome_cliente = models.CharField(max_length=100, null=True, blank=True)
