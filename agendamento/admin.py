from django.contrib import admin
from .models import Agendamento, Estabelecimento
# Register your models here.
admin.site.register(Estabelecimento)
admin.site.register(Agendamento)