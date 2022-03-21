from django.views.generic.edit import FormView

from pages.forms.agendamento.agendamentoForm import AgendamentoForm

class AgendamentoView(FormView):
    template_name = 'agendamento/agendamento.html'
    form_class = AgendamentoForm
    success_url= '/listagem/'
    
    def form_valid(self, form):
        form.agendar(self.request)
        return super().form_valid(form)