from django.urls import path
from .views import *

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("", inicio, name="inicio"),

    path("about/", about, name="about"),
    path("noHayPaginasAun/", noHayPaginasAun, name="noHayPaginasAun"),

    path("chat/", chat, name="chat"),
    
    path("enviarMensaje/", enviarMensaje, name="enviarMensaje"),

    path("recibir/", recibir, name="recibir"),
    path("recibirMensajes/", recibirMensajes, name="recibirMensajes"),

]