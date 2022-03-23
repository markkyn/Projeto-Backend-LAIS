from django.views import View

#Django HTTP
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# DJANGO AUTH API
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

#FORMS
from pages.forms import LoginForm

class LoginView(View):
    template_name = "authentication/login.html"

    def get(self, request):
        context = {
            'form': LoginForm()
        }

        return render( request, self.template_name, context )

    def post(self, request):
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            cpf = form.cleaned_data['cpf_Field']
            password = form.cleaned_data['password_Field']
            user = authenticate(cpf=cpf, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('pages:home'))
        
        context = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }     
        return render(request, self.template_name , context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('pages:home')

