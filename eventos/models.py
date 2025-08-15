from django.db import models

class Eventos(models.Model):
    # coloca campo de foto ?
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    local_evento = models.CharField(max_length=200)
    data_evento = models.DateField(help_text='Data para realização do evento')
    link = models.URLField(help_text='Link para site de inscrição do Evento')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_evento']
