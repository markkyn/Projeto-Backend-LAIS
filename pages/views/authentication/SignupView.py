from django.views.generic.edit import FormView

from pages.forms.authentication.SignupForm import SignupForm
from django.contrib import messages


class SignupView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignupForm
    success_url="/"

    def form_valid(self, form):
        form.register()

        messages.add_message(
                self.request,
                messages.SUCCESS,
                'Cadastro Realizado com Sucesso. Clique em "Entrar" para ser autenticado!'
        )

        return super().form_valid(form)