from django.contrib import admin
from aplicacao.models import Visitante,Morador

# Register your models here.
class MoradAdmin(admin.ModelAdmin):
    list_display = ['endereco','nome_completo']

class VisitAdmin(admin.ModelAdmin):
    list_display = ['nome_completo']

admin.site.register(Visitante)
admin.site.register(Morador)

admin.site.site_header = 'Administração de visitantes e moradores'
admin.site.site_title = 'Administração de visitantes e moradores'
