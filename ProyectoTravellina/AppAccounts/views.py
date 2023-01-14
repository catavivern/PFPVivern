from django.shortcuts import render

from AppAccounts.forms import SignupUserForm, EditProfileForm, AvatarForm

from AppMessages.views import noHayPaginasAun
from django.contrib.auth.views import LogoutView

from .models import Perfil

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


from django.contrib.auth.decorators import login_required


# Create your views here.
def inicioAppAccounts(request):
    return render (request, "AppAccounts/inicioAppAccounts.html")

#Vista de registro

def signup(request):
    if request.method=="POST":
        form= SignupUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "AppAccounts/inicioAppAccounts.html", {"mensaje": f"Usuario {username} creado correctamente", "avatar": obtainAvatar(request)})
        else:
            return render(request, "AppAccounts/signup.html", {"form":form, "mensaje":"Error al crear el usuario", "avatar": obtainAvatar(request)})
    else: 
        form= SignupUserForm()
        return render(request, "AppAccounts/signup.html", {"form": form, "avatar": obtainAvatar(request)})


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppAccounts/inicioAppAccounts.html", {"mensaje": f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppAccounts/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppAccounts/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppAccounts/login.html", {"form": form})

def profile(request):
    return render (request, "AppAccounts/profile/profile.html")


# funcion readProfile que me diga los datos del perfil. en el template poner un link a editProfile

def obtainAvatar(request):
    lista=Perfil.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/imagenAvatar/avatarpordefecto.png"
    return avatar

@login_required
def addAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Perfil(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Perfil.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppAccounts/profile/profile.html", {"mensaje":f"Foto de perfil agregada correctamente", "avatar": obtainAvatar(request)})
        else:
            return render(request, "AppAccounts/profile/addAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar la foto de perfil", "avatar": obtainAvatar(request)})
    else:
        form=AvatarForm()
        return render(request, "AppAccounts/profile/addAvatar.html", {"form": form, "usuario": request.user, "avatar": obtainAvatar(request)})


@login_required
def readProfile(request):
    perfiles=Perfil.objects.all()

    return render(request, "AppAccounts/profile/readProfile.html", {"perfiles": perfiles, "avatar": obtainAvatar(request)})


@login_required
def editProfile(request):
    usuario=request.user

    if request.method=="POST":
        form=EditProfileForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]            
            usuario.first_name=info["first_name"]            
            usuario.last_name=info["last_name"]
            usuario.descripcion=info["descripcion"]
            usuario.paginaWeb=info["paginaWeb"]
            usuario.save()
            return render(request, "AppAccounts/inicioAppAccounts.html", {"mensaje":f"Usuario {usuario.username} editado correctamente", "avatar": obtainAvatar(request)})
    else:
        form=EditProfileForm(instance=usuario)
        return render(request, "AppAccounts/profile/editProfile.html", {"form":form, "nombreusuario":usuario.username, "avatar": obtainAvatar(request)})         
#que edite username, deescripcion, link a pag web, email y contraseña

#funcion que elimine mi perfil
@login_required
def deleteProfile(request):
    perfil=Perfil.objects.all()
    print(perfil)
    perfil.delete()
    return render(request, "AppAccounts/profile/profile.html", {"mensaje": "Perfil eliminado correctamente, ahora apriete el botón de Logout porfavor", "avatar": obtainAvatar(request)})
