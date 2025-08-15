from django.db import models

class Editais(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.URLField(help_text='Link para o site oficial do edital')
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo