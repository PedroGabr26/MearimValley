from django.db import models

class Noticias(models.Model):
    foto = models.ImageField(upload_to='noticias/',null=True, blank=True)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_noticia = models.DateField(auto_now_add=True)