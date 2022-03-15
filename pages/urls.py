from django.urls import path, include

from .views.homeView import HomeView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]