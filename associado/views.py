from django.http import HttpResponse
from django.shortcuts import render
from associado.models import Associado,Empresa


def index(request):
    # dados mock do associado: ID, nome, status, (ativo/inativo)
    # criar uma lista de dicionários com dados mock para representar os usuários(associados)
    #Agora não vai precisar usar essa lista de dados, foi criado um banco de dados com o shell e sqlite
    """
    associados = [
        {'id': '001', 'nome': 'Romulo Jackson', 'status': 'Ativo'},
        {'id': '002', 'nome': 'David Quilan', 'status': 'Ativo'},
        {'id': '003', 'nome': 'Nayan Jonhson', 'status': 'Inativo'},
        {'id': '004', 'nome': 'Cassio Dylan', 'status': 'Ativo'},
        {'id': '005', 'nome': 'Welligton Clinton', 'status': 'Inativo'},
        {'id': '006', 'nome': 'Marcos Jordan', 'status': 'Pendente'},
        {'id': '007', 'nome': 'Lucio Smith', 'status': 'Ativo'},
        {'id': '008', 'nome': 'Robert Brown ', 'status': 'Ativo'},
        {'id': '009', 'nome': 'Mary Jackson', 'status': 'Inativo'},
        {'id': '010', 'nome': 'Enzo Smith', 'status': 'Pendente'},
        {'id': '011', 'nome': 'Wesley Cleriton', 'status': 'Ativo'},
        {'id': '012', 'nome': 'Dennis Jonhson', 'status': 'Inativo'},
    ]
        
    """
    ## Prepara o dicionário de contexto. 
    associados = Associado.objects.all()
    # O Django buscará automaticamente dentro da pasta templates/
    return render(request, 'associado/index.html', {'lista_associados': associados})
# Função para carregar o perfil do associado


def perfil(request):
    return render(request, 'associado/perfil.html')


def beneficios(request):
    # Por enquanto, apenas renderizamos o HTML de design
    return render(request, 'associado/beneficios.html')


def carteirinha(request):
    # Aqui passamos o contexto 'vibe pwa' para o template
    return render(request, 'associado/carteirinha.html')

def empresa(request):
    # Aqui passamos o contexto 
    empresa = Empresa.objects.all()
    return render(request, 'associado/empresa.html',{"empre":empresa})