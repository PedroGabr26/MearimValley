from django.db import models

class Parceiro(models.Model):
    logo_empresa = models.ImageField(upload_to='logos/',null=True, blank=True)
    nome_empresa = models.CharField(max_length=100)
    site = models.URLField()
    descricao = models.TextField()
    email = models.EmailField(unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome