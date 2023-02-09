from django.db import models
from datetime import datetime    
from cpf_field.models import CPFField
from django.core.exceptions import ValidationError

class Visitante(models.Model):

    CPF = CPFField('CPF',primary_key=True)
    nome_completo = models.CharField(null = False,max_length=100,verbose_name = "Nome Completo")
    placa = models.CharField(max_length=7,verbose_name= "Placa")
    telefone = models.CharField(max_length=14,null=False,verbose_name ="Telefone" )
    hora_entrada = models.DateTimeField(default=datetime.now, blank=True,verbose_name="Horário de Entrada")
    hora_saida = models.DateTimeField(null=True,blank=True,verbose_name="Horário de Saída")

    class Meta:
        verbose_name_plural = "Visitante"
        db_table = "Visitante"
        ordering = ['nome_completo']   

    def __str__(self):
        return f'{self.nome_completo},{self.hora_entrada}'

class Morador(models.Model):

    CPF = CPFField('CPF',primary_key=True)
    nome_completo = models.CharField(null = False,max_length=100,verbose_name = "Nome Completo")
    endereco = models.CharField(null = False,max_length=100,verbose_name = "Endereço")
    numero = models.CharField(null = False,max_length=4,verbose_name = "Número")
    placa = models.CharField(max_length=7,verbose_name= "Placa")
    telefone = models.CharField(max_length=14,null=False,verbose_name ="Telefone" )
    hora_entrada = models.DateTimeField(default=datetime.now, blank=True,verbose_name="Horário de Entrada")
    hora_saida = models.DateTimeField(null=True,blank=True,verbose_name="Horário de Saída")

    class Meta:
        verbose_name_plural = "Morador"
        db_table = "Morador"
        ordering = ['endereco','nome_completo']
    def __str__(self):
        return f'{self.endereco},{self.nome_completo}'
