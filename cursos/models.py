from django.db import models

class Cursos(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.URLField(help_text='Link da página do curso ofertado')
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo