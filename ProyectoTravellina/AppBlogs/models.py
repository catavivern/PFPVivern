from django.db import models

# Create your models here.

class Blog(models.Model):
    titulo= models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=400)
    autor=models.CharField(max_length=50)
    emailAutor=models.EmailField(max_length=50)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to="imagenBlogs")


