#models.py
from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(max_length=30)
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    peso = models.IntegerField()