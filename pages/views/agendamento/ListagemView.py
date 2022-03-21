from django.shortcuts import render
from django.views import View

from agendamento.models import Agendamento

class ListagemView(View):
    model = Agendamento
    template_name = 'agendamento/listagem.html'

    def get(self,request):
        context = {
            'agendamento': Agendamento.objects.all()
        }

        return render(request, self.template_name, context)