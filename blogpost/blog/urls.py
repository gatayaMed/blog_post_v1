from django.urls import path

from . views import HomeView,PostDetails
urlpatterns = [
    
     #path('', views.home, name='home'),
     path('',HomeView.as_view(), name='home' ),
     path('article/<int:pk>',PostDetails.as_view(), name='postdetails' ),

    
     
]