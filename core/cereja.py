from rest_framework import serializers
from .models import Produto, Categoria
from rest_framework import serializers
from .models import Livro, Emprestimo

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'categoria']


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'

    def validate(self, data):
        livro = data.get('livro')
        devolvido = data.get('devolvido', False)

        if not devolvido:
            emprestimos_abertos = Emprestimo.objects.filter(livro=livro, devolvido=False)
            if self.instance:
                emprestimos_abertos = emprestimos_abertos.exclude(pk=self.instance.pk)
            
            if emprestimos_abertos.exists():
                raise serializers.ValidationError({"livro": "Este livro já possui um empréstimo ativo (Não Devolvido)."})
        return data