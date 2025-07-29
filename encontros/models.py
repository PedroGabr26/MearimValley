from django.db import models

class Encontros(models.Model):
    titulo = models.TextField(max_length=200)
    descricao = models.TextField()
    local_encontro = models.CharField(max_length=255)
    data_encontro = models.DateField(help_text='Data para realização do encontro')
    data_criacao = models.DateTimeField(auto_now_add=True)
    link = models.URLField(help_text='Link para inscrição do encontro')

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-data_encontro"]