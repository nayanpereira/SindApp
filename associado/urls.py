from django.urls import path
from associado import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.perfil, name='perfil'),
    path('beneficios/', views.beneficios, name='beneficios'),
    path('minha-carteirinha/', views.carteirinha, name='minha-carteirinha'),
    path('empresa/', views.empresa, name='empresa'),
]