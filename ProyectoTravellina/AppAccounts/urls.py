from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicioAppAccounts/", inicioAppAccounts, name="inicioAppAccounts"),
    path("", inicioAppAccounts, name="inicioAppAccounts"),

    path("noHayPaginasAun/", noHayPaginasAun, name="noHayPaginasAun"),

    path("signup/", signup, name="signup"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/profile/", profile, name="profile"),
    path("profile/readProfile/", readProfile, name="readProfile"),
    path("profile/editProfile/", editProfile, name="editProfile"),
    path("profile/deleteProfile", deleteProfile, name="deleteProfile"),
    path("profile/addAvatar/", addAvatar, name="addAvatar"),



] 