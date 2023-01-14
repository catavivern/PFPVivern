from django import forms

from .models import Mensaje

class MensajeForm(forms.Form):

    emisor= forms.CharField(max_length=50)
    receptor=forms.CharField(max_length=50)
    cuerpo= forms.CharField(max_length=20)
    leido= forms.BooleanField()

    class Meta:
        model=Mensaje
        fields=["emisor", "receptor", "cuerpo", "leido", "horario"] 
        help_texts = {k: "" for k in fields}

