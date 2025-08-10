from django.db import models

class Corporativos(models.Model):
    logo = models.ImageField(upload_to='logos/',null=True, blank=True)
    nome = models.CharField(max_length=200)
    sobre = models.TextField()
    link = models.URLField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

