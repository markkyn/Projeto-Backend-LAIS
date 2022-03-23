from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import LogoutView, LoginView, SignupView, HomeView, dropdownView
from agendamento.views import AgendamentoView, ListagemView

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