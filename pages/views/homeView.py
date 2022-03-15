from django.views import View
from django.shortcuts import render

from users.models import User

class HomeView(View):
    model = User
    template_name = 'home.html'

    def get(self, request):
        return(render(request, self.template_name, context = {'user' : request.user} ))