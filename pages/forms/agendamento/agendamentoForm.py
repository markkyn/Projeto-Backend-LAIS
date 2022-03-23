import re
from urllib import request
from django import forms
from agendamento.models import Estabelecimento, Agendamento
import datetime as dt

class AgendamentoForm(forms.Form):
    estabelecimento_Field = forms.ModelChoiceField(
        label= "Estabelecimentos",
        queryset=Estabelecimento.objects.all()
    )
    
    horario_Field = forms.ModelChoiceField(
        label= "Horários Disponiveis",
        queryset= Agendamento.objects.none()
    )

    def agendar(self, request):

        if 'estabelecimento_Field' in self.data:
            estabelecimento_id = int(self.data.get('estabelecimento_Field'))
            self.fields['horario_Field'].queryset = Agendamento.objects.filter(estabelecimento_id = estabelecimento_id)

            horario_formatado = re.search(r'\((.*?)\)',self.data.get('horario_Field')).group(1)\
                .split(sep=':')
            
            data_formatada = re.search(r'\,(.*?)\(',self.data.get('horario_Field')).group(1)\
                .strip(' ')\
                .split(sep = '-')
            
            # Partes do Horario_formatado
            hora     = int(horario_formatado[0])
            minutos  = int(horario_formatado[1])
            segundos = int(horario_formatado[2])

            # Partes da data_formatada
            ano = int(data_formatada[0])
            mes = int(data_formatada[1])
            dia = int(data_formatada[2])

            # Agendamento Selecionado
            agendamento = Agendamento.objects\
                .filter(estabelecimento_id = estabelecimento_id) \
                .filter(appointment_hour = dt.time(hora, minutos, segundos))\
                .filter(appointment_date = dt.date(ano, mes, dia))\
                .first() # Queryset -> Agendamento
            
            # Verifica se o Agendamento tem menos de 5 usuários cadastrados (vagas livres)
            # e se o Usuário tem algum agendamento não expirado
            # ou o caso em que o Usuário não tem nenhum agendamento cadastrado
            if  ( agendamento.users.count() < 5 and self.has_no_expired_appointment(request.user) ) \
            or  not agendamento:
                agendamento.users.add(request.user)
            else:
                raise forms.ValidationError("Impossibilitado de realizar agendamento - Você já tem um agendamento não-expirado ou não há vagas para esse agendamento")
        elif self.instance.pk:
            self.fields['horario_Field'].queryset = self.instance.establecimento_Field

    def has_no_expired_appointment(self, user):
        if(Agendamento.objects.filter(users = user).exists()):
            for user_appointment in Agendamento.objects.filter(users = user):
                if(user_appointment.is_expired == False):
                    return False
            return True
        else:
            return True