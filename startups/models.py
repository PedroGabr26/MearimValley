from django.db import models

class Startup(models.Model):
    logo_startup = models.ImageField(upload_to='logos/',null=True, blank=True)
    nome_startup = models.CharField(max_length=100)
    descricao_startup = models.TextField()
    site = models.URLField(help_text='Link para o site da startup')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_startup

