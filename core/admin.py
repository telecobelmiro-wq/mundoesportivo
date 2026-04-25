from django.contrib import admin

# Register your models here.
from .models import Categoria, Produto, Pedido

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)