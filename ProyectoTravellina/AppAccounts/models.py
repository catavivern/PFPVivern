from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    imagen=models.ImageField(upload_to="imagenAvatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    paginaWeb=models.URLField(max_length=200)

    def __self__(self):
        return f"{self.first_name} {self.last_name}"