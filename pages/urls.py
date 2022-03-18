from django.urls import path, include

from .views.HomeView import HomeView
from .views.SignupView import SignupView
from .views.LoginView import LoginView, LogoutView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name= 'signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout")
]