from datetime import time
from agendamento.models import Agendamento
from django.shortcuts import render

# DropDown Dependent List (View)
def send_horarios_data(request):
    template = 'utils/dropDownList.html'
    
    estabelecimento_pk = request.GET.get('estabelecimento')

    user_age = request.user.get_idade()
    horarios = get_horario(user_age)

    agendamentos_filtrados = [ x for x in 
      Agendamento.objects.filter(estabelecimento__id = estabelecimento_pk)\
      .exclude(appointment_hour__lt = horarios[0])\
      .exclude(appointment_hour__gt = horarios[1])

      if x.users.count() < 5
    ]
        
    return render(request, template, {"agendamentos": agendamentos_filtrados})

def get_horario(idade):
    idades = [
        idade >= 18 and idade <= 29,
        idade >= 30 and idade <= 39,
        idade >= 40 and idade <= 49,
        idade >= 50 and idade <= 59,
        idade >= 60                
    ]

    horarios = [
        (time(13), time(13,59)),
        (time(14), time(14,59)),
        (time(15), time(15,59)),
        (time(16), time(16,59)),
        (time(17), time(17,59)),
    ]

    i=0
    for b_idade in idades:
        if b_idade == True:
            return horarios[i]
        i = i+1