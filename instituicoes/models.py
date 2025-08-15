from django.db import models

class Instituicoes(models.Model):
    logo_instituicao = models.ImageField(upload_to='logos/',null=True, blank=True)
    nome_instituicao = models.CharField(max_length=200)
    descricao_instituicao = models.TextField()
    link_site = models.URLField(help_text='Link para site da instituição')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_instituicao
    
