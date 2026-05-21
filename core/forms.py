from django import forms
from .models import Produto
from .models import Livro, Emprestimo

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

from django import forms
from .models import Livro, Emprestimo

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'pessoa', 'devolvido']

    def clean(self):
        cleaned_data = super().clean()
        livro = cleaned_data.get('livro')
        devolvido = cleaned_data.get('devolvido')

        if livro and not devolvido:
            emprestimos_abertos = Emprestimo.objects.filter(livro=livro, devolvido=False)
            if self.instance.pk:
                emprestimos_abertos = emprestimos_abertos.exclude(pk=self.instance.pk)
            
            if emprestimos_abertos.exists():
                raise forms.ValidationError(f"O livro '{livro.titulo}' já possui um empréstimo ativo e não foi devolvido.")
        
        return cleaned_data