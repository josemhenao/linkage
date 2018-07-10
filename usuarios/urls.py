from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UsuariosView, RegisterView, LoginView, ChangePasswordView, LogoutView, ProfileView, DeleteView

urlpatterns = [
    path('', UsuariosView.as_view(), name='usuarios'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('<str:username>', ProfileView, name='usuario_profile'),
    path('<str:username>/cambiar_password', ChangePasswordView.as_view(), name='change_password'),
    path('eliminar_cuenta/<str:username>', DeleteView, name='eliminar_cuenta' )
]
