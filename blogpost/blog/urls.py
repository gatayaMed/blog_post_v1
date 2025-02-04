from django.urls import path

from . views import HomeView,PostDetails,AddPostView,UpdatePostView
urlpatterns = [
    
     #path('', views.home, name='home'),
     path('',HomeView.as_view(), name='home' ),
     path('article/<int:pk>',PostDetails.as_view(), name='postdetails' ),
     path('addpost/',AddPostView.as_view(), name='addpost' ),
     path('article/edit/<int:pk>',UpdatePostView.as_view(), name='updatepost' ),

    
     
]