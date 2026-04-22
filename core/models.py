from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem_url = models.URLField(max_length=500, blank=True, help_text="file:///C:/Users/THALISSIQUEIRABELMIR/Downloads/Gemini_Generated_Image_rb1i1irb1i1irb1i.png")

    def __str__(self):
        return self.nome