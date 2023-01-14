from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupUserForm(UserCreationForm):

    email= forms.EmailField(label="Email de usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class EditProfileForm(UserCreationForm):

    email= forms.EmailField(label="Email de usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar nombre")
    last_name=forms.CharField(label="Modificar apellido")
    descripcion=forms.CharField(label="Modificar descripción")
    paginaWeb=forms.URLField(label="Modificar página web")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name", "descripcion", "paginaWeb"] #agregar los campos que faltan
        help_texts = {k: "" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
