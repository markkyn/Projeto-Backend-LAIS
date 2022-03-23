from django.contrib import admin
from .models import Agendamento, Estabelecimento
# Register your models here.

@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('nome','cnes')
    
    list_filter = ('cnes', 'nome')
    search_fields = ['cnes', 'nome']

admin.site.register(Agendamento)