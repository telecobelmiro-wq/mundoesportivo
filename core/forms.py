from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['categoria', 'nome', 'preco', 'imagem_url']

        labels = {
            'categoria': 'Categoria',
            'nome': 'Nome',
            'preco': 'Preço',
            'imagem_url': 'URL da Imagem',
        }

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
