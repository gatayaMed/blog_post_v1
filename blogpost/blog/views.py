from django.shortcuts import render
from . models import Post, Category
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
    
    def get_context_data(self,*args ,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        
        context["cat_menu"] = cat_menu 
        return context


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


class AddCategoryView(CreateView):
    model = Category 
    template_name = 'addcategory.html'
    fields = '__all__'    


def CategoryView(request, cats):

    category_posts = Post.objects.filter(category=cats.replace('-',' '))

    return render (request, 'categories.html',{'cats':cats.replace('-',' '), 'category_posts': category_posts})


def Category_List_View(request):

    category_list = Category.objects.all()

    return render (request, 'category_list_view.html',{'category_list':category_list})