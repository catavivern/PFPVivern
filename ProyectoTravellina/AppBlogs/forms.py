from django import forms

class BlogForm(forms.Form):
    titulo= forms.CharField(label="Título", max_length=50)
    subtitulo= forms.CharField(label="Subtítulo", max_length=50)
    cuerpo= forms.CharField(label="Cuerpo", max_length=400)
    autor= forms.CharField(label="Autor", max_length=50)
    emailAutor=forms.EmailField(label="Email del autor", max_length=50)
    fecha=forms.DateField(label="Fecha")
    imagen=forms.ImageField(upload_to="imagenBlogs")



