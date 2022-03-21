from django import forms
from agendamento.models import Estabelecimento, Agendamento
import datetime as dt

class AgendamentoForm(forms.Form):
    estabelecimento_Field = forms.ModelChoiceField(
        queryset=Estabelecimento.objects.all()
    )
    
    horario_Field = forms.ModelChoiceField(
        queryset= Agendamento.objects.all()
    )

    def agendar(self, request):
        pass