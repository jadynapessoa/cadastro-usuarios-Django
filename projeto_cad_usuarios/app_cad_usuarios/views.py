from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request): # função que faz a requisição para home
    return render(request,'usuarios/home.html') # renderizando e criando uma página

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    # Exibir usuários cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar os dados para a página de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)