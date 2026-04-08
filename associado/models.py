from django.db import models
from django.core.exceptions import ValidationError

class Empresa(models.Model):
    orgao = models.CharField("Órgão/Empresa", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=14)
    ativo = models.BooleanField(default=True)
    nome_contato = models.CharField("Nome do Contato", max_length=100)

    def clean(self):
        # Exemplo: remover pontos e traços antes de validar (caso o usuário digite com máscara)
        self.cnpj = ''.join(filter(str.isdigit, self.cnpj))
        
        # Verifica se já existe outra empresa com este CNPJ (excluindo a própria empresa em caso de edição)
        if Empresa.objects.filter(cnpj=self.cnpj).exclude(pk=self.pk).exists():
            raise ValidationError({'cnpj': "Já existe uma empresa cadastrada com este CNPJ."})

    def __str__(self):
        return f"{self.orgao} - CNPJ: {self.cnpj}"

    class Meta:
        db_table = 'empresa'

class Associado(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    # Relação N:1 (Muitos associados para uma empresa)
    empresa = models.ForeignKey(Empresa, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='associados'
    )

    def __str__(self):
        status = "Ativo" if self.ativo else "Inativo"
        return f"{self.nome} - {status}"
    
    class Meta:
        db_table = 'associado'

class Endereco(models.Model):
    logradouro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    # Permite ligar a um Associado OU a uma Empresa
    associado = models.OneToOneField('Associado', on_delete=models.CASCADE, null=True, blank=True, related_name='endereco')
    empresa = models.OneToOneField('Empresa', on_delete=models.CASCADE, null=True, blank=True, related_name='endereco_empresa')

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}"
    
    # definir o nome da tabela
    class Meta:
        db_table = 'endereco'