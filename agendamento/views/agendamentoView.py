from django.forms import ValidationError
from django.views.generic.edit import FormView
from django.utils.translation import gettext_lazy as _

from django.contrib import messages

from agendamento.forms import AgendamentoForm

class AgendamentoView(FormView):
    template_name = 'agendamento/agendamento.html'
    form_class    = AgendamentoForm
    success_url   = '/listagem/'
    
    #Por conta do DropDownList, a validação fica por conta do AgendamentoForm 
    def form_invalid(self, form):
        try:
            form.agendar(self.request)
        except ValueError: # Caso o Usuário nao coloque um estabelecimento o formulario irá subir um Value Error por conta do estabelecimento_id ser ""
                           #, impossibilitando o casting [ int(estabelecimento_id) ]
            messages.add_message(
                self.request,
                messages.ERROR,
                "Estabelecimento Inválido - Por favor, selecione um Estabelecimento válido"
            )
        
        except AttributeError as e: # Caso o Usuário não selecione um Horário
            messages.add_message(
                self.request,
                messages.ERROR,
                "Horário Inválido - Por favor, selecione um horário válido"
            )
        
        except ValidationError as e: # Caso o Usuário já esteja cadastrado ou não haja vagas no agendamento Selecionado
            messages.add_message(
                self.request,
                messages.ERROR,
                e.message
            )
        
        except: # Qualquer outro caso
            messages.add_message(
                self.request,
                messages.ERROR,
                "Ocorreu um erro no agendamento"
            )
            
        return super().form_valid(form) # Em todos os casos ele é enviado à listagem, caso haja erro haverá um botão para voltar para o agendamento
        