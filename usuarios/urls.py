from django.urls import path

from .views import RegisterView, LoginView, AuthView, UpdateUsuarioView, DeleteUsuarioView, LogoutView, DetalleUsuarioView

urlpatterns = [
    path('', AuthView.as_view(), name='auth'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('update', UpdateUsuarioView.as_view(), name='update'),
    path('delete/<slug:slug>', DeleteUsuarioView.as_view(), name='delete'),
    path('<slug:slug>', DetalleUsuarioView.as_view(), name='detail_user'),
]
