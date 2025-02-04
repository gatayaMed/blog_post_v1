from django.urls import path

from . views import HomeView,PostDetails,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,Category_List_View
urlpatterns = [
    
     #path('', views.home, name='home'),
     path('',HomeView.as_view(), name='home' ),
     path('article/<int:pk>',PostDetails.as_view(), name='postdetails' ),
     path('addpost/',AddPostView.as_view(), name='addpost' ),
     path('article/edit/<int:pk>',UpdatePostView.as_view(), name='updatepost' ),
     path('article/<int:pk>/remove',DeletePostView.as_view(), name='deletepost' ),
     path('addcategory/',AddCategoryView.as_view(), name='addcategory' ),
     path('category/<str:cats>/',CategoryView, name='category' ), 
     path('category_list_view/',Category_List_View, name='category_list' ),
]