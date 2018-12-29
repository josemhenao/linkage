from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UsuariosView, RegisterView, LoginView, ChangePasswordView, ChangeImageView, \
    LogoutView, ProfileView, DeleteView, ProfileView, DeleteView, UpdateView

urlpatterns = [
    #path('', UsuariosView.as_view(), name='usuarios'),
    path('register', RegisterView.as_view(), name='usuarios_register'),
    path('login', LoginView.as_view(), name='usuarios_login'),
    path('logout', LogoutView.as_view(), name='usuarios_logout'),
    path('<slug:slug>/profile', ProfileView.as_view(), name='usuarios_profile'),
    path('<slug:slug>/update', UpdateView.as_view(), name='usuarios_update'),
    path('<str:username>/cambiar_password', ChangePasswordView.as_view(), name='usuarios_change_password'),
    path('<str:username>/cambiar_imagen', ChangeImageView.as_view(), name='usuarios_change_image'),
    path('<slug:slug>/eliminar_cuenta', DeleteView.as_view(), name='usuarios_delete')
]
