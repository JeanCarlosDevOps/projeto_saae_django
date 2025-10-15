# Dentro do arquivo avisos/admin.py

from django.contrib import admin
from .models import Bairro, AvisoFaltaDagua

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(AvisoFaltaDagua)
class AvisoFaltaDaguaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_inicio_previsto', 'data_fim_previsto')
    list_filter = ('status', 'bairros_afetados')
    search_fields = ('titulo', 'mensagem')
    filter_horizontal = ('bairros_afetados',) # Melhora MUITO a interface para selecionar bairros