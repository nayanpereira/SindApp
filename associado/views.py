from django.shortcuts import render

def index(request):
    # criar dados mock do associado: ID, nome, status, (ativo/inativo)
    # criar uma lista de dicionários com dados mock para representar os usuários
    associado = [
    {'id':'001','nome':'Romulo Jackson','status':'Ativo'},
    {'id':'002','nome':'David Quilan','status':'Ativo'},
    {'id':'003','nome':'Nayan Jonhson','status':'Inativo'},
    {'id':'004','nome':'Cassio Dylan','status':'Ativo'},
    {'id':'005','nome':'Welligton Cliton','status':'Inativo'},
    ]
    # O django buscara automaticamente dentro da pasta templates
    # 2. Prepara o dicionário de contexto. 
    # A chave 'lista_associado' é exatamente o nome que você usou no {% for %} do HTML.
    contexto = {
        'lista_associado': associado
    }
    # 3. Passa o contexto como terceiro argumento no render
    return render(request, 'associado/index.html', contexto)

def perfil(request):
    return render(request, 'associado/perfil.html')

def beneficios(request):
    return render(request, 'associado/beneficios.html')

def carteirinha(request):
    return render(request, 'associado/carteirinha.html')