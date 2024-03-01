
from django.urls import path
from app_cad_usuarios import views
urlpatterns = [
    # rota, views responsável, nome de referência
    
    #facebook.com
    #path('') # coloca uma string vazia
    # facebook.com/devaprender
    #path('devaprender/')
    
    # usuarios.com
    path('',views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]
