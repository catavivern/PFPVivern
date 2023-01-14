from django.shortcuts import render
from .models import Mensaje
from .forms import MensajeForm

from AppAccounts.models import Perfil

from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render (request, "AppMessages/inicio.html")

def about(request):
    return render (request, "AppMessages/about.html")

@login_required
def chat(request):
    return render (request, "AppMessages/chat.html")


def noHayPaginasAun(request):
    return render (request, "AppMessages/noHayPaginasAun.html")

@login_required
def enviarMensaje(request):
    if request.method=="POST":
            form= MensajeForm(request.POST)
           
            if form.is_valid():
                informacion=form.cleaned_data #convierte de la info en modo formulario a un diccionario
                print(informacion)
                emisor= informacion["emisor"]
                receptor=informacion["receptor"]
                cuerpo=informacion["cuerpo"]
                leido=informacion["leido"]

                mensaje= Mensaje(emisor=emisor, receptor=receptor, cuerpo=cuerpo, leido=leido)
                mensaje.save()
                return render(request, "AppMessages/chat.html" ,{"mensaje": "Mensaje enviado correctamente"})
            else:
                return render(request, "AppAccounts/enviarMensaje.html" ,{"form": form, "mensaje": "Informacion no válida"})
            
    else:
        formulario= MensajeForm()
        return render (request, "AppMessages/enviarMensaje.html", {"form": formulario})


#recibirMensaje

@login_required
def recibirMensajes(request):
    return render(request, "AppMessages/recibirMensajes.html")

@login_required
def recibir(request):
    
    receptor= request.GET["receptor"]
    if receptor!="":
        mensajes= Mensaje.objects.filter(receptor__icontains=receptor)
        return render(request, "AppMessages/resultadosMensajes.html", {"mensajes": mensajes})
    else:                                   #antes decía resultadosBusqueda.html
        return render(request, "AppMessages/recibirMensajes.html", {"mensaje": "Ingrese su nombre correctamente para buscar las selecciones"})

