from django.http import HttpResponse
from django.shortcuts import render
from associado.models import Associado,Empresa
from django.utils import timezone
from datetime import timedelta


def index(request):
    # 1. Pegar o termo de busca enviado pelo formulário
    termo_busca = request.GET.get('buscar')

    # 2. Se o usuário digitou algo, filtramos. Se não, pegamos todos.
    if termo_busca:
        # icontains busca nomes que CONTÉM o texto, ignorando maiúsculas/minúsculas
        associados = Associado.objects.filter(nome__icontains=termo_busca)
    else:
        associados = Associado.objects.all().order_by('-data_cadastro') # Mais recentes primeiro

    # 3. Lógica para os Cards (Números Reais) e Card Inativos e pendentes, Vamos usar os inativos como exemplo
    total_ativos = Associado.objects.filter(ativo=True).count()
    total_pendentes = Associado.objects.filter(ativo=False).count()
    
    # NOVAS ADESÕES: Filtra quem cadastrou de 30 dias atrás até hoje
    trinta_dias_atras = timezone.now() - timedelta(days=30)
    novas_adesoes = Associado.objects.filter(data_cadastro__gte=trinta_dias_atras).count()

    contexto = {
        'lista_associados': associados,
        'total_ativos': total_ativos,
        'novas_adesoes': novas_adesoes,
        'total_pendentes': total_pendentes,
    }

    return render(request, 'associado/index.html', contexto)
    # Funções para carregar o perfil do associado


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