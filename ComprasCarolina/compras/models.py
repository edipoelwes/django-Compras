from django.db import models

class Compras(models.Model):
    nome = models.CharField(max_length=50)
    descricaoProduto = models.TextField()
    unidadeCompra = models.CharField(max_length=50)
    qtdPrevistoMes = models.DecimalField(max_digits=5, decimal_places=2)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    precoMaximo = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.nome
