from django.db import models

class Produtos(models.Model):
    produto =models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")
    descricao = models.TextField(max_length=300)
    data_validade = models.DateField()
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.produto

