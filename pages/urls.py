from django.urls import path, include

from .views.authentication.HomeView import HomeView
from .views.authentication.SignupView import SignupView
from .views.authentication.LoginView import LoginView, LogoutView

from .views.agendamento.AgendamentoView import AgendamentoView
from .views.agendamento.ListagemView import ListagemView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name= 'signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('agendamento/', AgendamentoView.as_view(), name="agendamento"),
    path('listagem/', ListagemView.as_view(), name="listagem"),
    
]