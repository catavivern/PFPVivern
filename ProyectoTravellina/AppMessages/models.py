from django.db import models

# Create your models here.


class Mensaje(models.Model):
    emisor= models.CharField(max_length=50)
    receptor= models.CharField(max_length=50)
    cuerpo= models.CharField(max_length=20)
    leido= models.BooleanField()

    def __str__(self):
        return f"Mensaje de {self.emisor} para {self.receptor}"