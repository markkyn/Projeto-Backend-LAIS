from django.views.generic.edit import FormView

from pages.forms.agendamento.agendamentoForm import AgendamentoForm

class AgendamentoView(FormView):
    template_name = 'agendamento/agendamento.html'
    form_class = AgendamentoForm
    success_url= '/listagem/'
    
    #Por conta do DropDownList, a validação fica por conta do AgendamentoForm 
    def form_invalid(self, form):
        form.agendar(self.request)
        return super().form_valid(form)