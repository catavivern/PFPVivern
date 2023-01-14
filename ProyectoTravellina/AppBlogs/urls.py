from django.urls import path
from .views import *

urlpatterns = [
    path("pages/", pages, name="pages"),
    path("", pages, name="pages"),

    path("noHayPaginasAun/", noHayPaginasAun, name="noHayPaginasAun"),
    path("leerMasBlog/<id>", leerMasBlog, name="leerMasBlog"),
    #path("leerMasTemplate", leerMasTemplate, name="leerMasTemplate")

]