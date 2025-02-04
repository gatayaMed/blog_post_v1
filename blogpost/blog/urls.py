from django.urls import path

from . views import HomeView,PostDetails,AddPostView
urlpatterns = [
    
     #path('', views.home, name='home'),
     path('',HomeView.as_view(), name='home' ),
     path('article/<int:pk>',PostDetails.as_view(), name='postdetails' ),
     path('addpost/',AddPostView.as_view(), name='addpost' ),

    
     
]