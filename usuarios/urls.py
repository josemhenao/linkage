from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView, LoginView, AuthView, ChangePasswordView, LogoutView, ProfileView

urlpatterns = [
    path('', AuthView.as_view(), name='usuarios'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('<str:username>', ProfileView, name='usuario_profile'),
    path('profile/change_password', ChangePasswordView, name='change_password'),
]
