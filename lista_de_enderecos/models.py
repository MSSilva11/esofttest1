from django.db import models

# Create your models here.

class Dados(models.Model):
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=60)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)
    descricao = models.TextField(max_length=100, blank=True)