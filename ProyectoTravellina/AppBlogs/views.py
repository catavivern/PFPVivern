from django.shortcuts import render

from AppMessages.views import noHayPaginasAun
from AppBlogs.models import Blog

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def pages(request):
    blogs=Blog.objects.all()
    return render (request, "AppBlogs/pages.html", {"blogs":blogs})

@login_required
def leerMasBlog(request, id):
    blog=Blog.objects.get(id=id)
    return render(request, "AppBlogs/leerMasTemplate.html", {"blog":blog })

@login_required
def noHayPaginasAun(request):
    return render (request, "AppBlogs/noHayPaginasAun.html")