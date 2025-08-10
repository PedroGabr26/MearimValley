from django.db import models

class Ambiente(models.Model):
    logo_ambiente = models.ImageField(upload_to='logos/',null=True, blank=True)
    sobre_ambiente = models.TextField()
    site_ambiente = models.URLField(help_text='Link do site referente ao ambiente')

    def __str__(self):
        return self.id
