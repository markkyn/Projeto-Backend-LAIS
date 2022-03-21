from typing import Type
from django import forms
from agendamento.models import Estabelecimento, Agendamento
import datetime as dt

class AgendamentoForm(forms.Form):
    estabelecimento_Field = forms.ModelChoiceField(
        queryset=Estabelecimento.objects.all()
    )
    
    horario_Field = forms.ModelChoiceField( 
        queryset= Agendamento.objects.none()
    )

    def agendar(self, request):

        if 'estabelecimento_Field' in self.data:
            try:
                estabelecimento_id = int(self.data.get('estabelecimento_Field'))
                self.fields['horario_Field'].queryset = Agendamento.objects.filter(estabelecimento_id = estabelecimento_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['horario_Field'].queryset = self.instance.establecimento_Field



       