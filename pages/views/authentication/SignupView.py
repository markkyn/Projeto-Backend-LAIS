from django.views.generic.edit import FormView

from pages.forms.authentication.SignupForm import SignupForm

class SignupView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignupForm
    success_url="/"

    def form_valid(self, form):
        form.register()
        return super().form_valid(form)