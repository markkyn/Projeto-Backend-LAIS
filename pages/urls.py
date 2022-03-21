from django.urls import path, include

from .views.authentication.HomeView import HomeView
from .views.authentication.SignupView import SignupView
from .views.authentication.LoginView import LoginView, LogoutView

from .views.agendamento.AgendamentoView import AgendamentoView
from .views.agendamento.ListagemView import ListagemView

from .views.utils import dropdownView
from django.contrib.auth.decorators import login_required

app_name = 'pages'

urlpatterns = [
    
    # Non-LoginRequired URLs
    path('', HomeView.as_view()         , name='home'),
    path('signup/', SignupView.as_view(), name= 'signup'),
    path('login/', LoginView.as_view()  , name='login'),
    
    #Login Required URLs
    path('logout/'      , login_required(LogoutView.as_view())      , name="logout"),
    path('agendamento/' , login_required(AgendamentoView.as_view()) , name="agendamento"),
    path('listagem/'    , login_required(ListagemView.as_view())    , name="listagem"),
    
    #UTILS
    path('ajax/carregar-horarios/', dropdownView.send_horarios_data, name="ajax_carregar_horarios" ) #Dependent DropDownList

]