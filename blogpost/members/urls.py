from django.urls import path
from .views import UserRegisterView  


urlpatterns = [
    
    #path('', views.home, name='home'),
    path('',UserRegisterView.as_view(), name='register' ),
    
     
     
]
