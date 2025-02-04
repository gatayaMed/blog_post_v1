from django.shortcuts import render
from . models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm ,EditForm
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
   # return  render (request, 'home.html', {})

class HomeView(ListView):
    model = Post 
    template_name = 'home.html'
    #ordering = ['-id'] # order post by negative id 
    ordering = ['-post_date']  #  ordering the posts by date   



class PostDetails(DetailView):
    model = Post
    template_name= 'postdetails.html'



class AddPostView(CreateView):
    model = Post
    form_class = PostForm # we use this line form_class when we want to show the fields  from our forms.py not automatic 
    template_name = 'addpost.html'
    success_url = reverse_lazy('home')  # ensures that Django knows where to redirect after a successful form submission.
    #fields = '__all__'
    #  here instead of showing all the fields in the post model  we can do it manually like that :
    # fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'
    success_url = reverse_lazy('home')  # Change 'home' to the actual name of the page you want to redirect to
    #fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')