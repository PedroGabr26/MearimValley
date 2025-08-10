from django.db import models

class Profissionais(models.Model):
    nome = models.CharField(max_length=200)
    sobre = models.TextField()
    rede_social = models.URLField()

    def __str__(self):
        return self.nome
