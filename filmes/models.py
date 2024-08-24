from django.db import models

# Create your models here.

class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=50)
    sinopse = models.TextField(blank=True, null=True)
    informacoes_adicionais = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo    