from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"
