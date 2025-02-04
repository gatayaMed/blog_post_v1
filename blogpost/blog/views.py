from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView,DeleteView
from . models import Post,Category
from .forms import PostForm ,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.
#ef home(request):
 #  return  render (request, 'home.html', {})

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


    def get_context_data(self,*args ,**kwargs):
          cat_menu = Category.objects.all()
          context = super(PostDetails, self).get_context_data(*args, **kwargs)
          stuff = get_object_or_404(Post, id=self.kwargs['pk'])
          total_likes =stuff.total_likes()
          
          liked =False 
          if stuff.likes.filter(id=self.request.user.id).exists():
              liked =True
             
              

          context["cat_menu"] = cat_menu 
          context["total_likes"] = total_likes
          context["liked"] = liked
          return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm # we use this line form_class when we want to show the fields  from our forms.py not automatic 
    template_name = 'addpost.html'
    #fields = '__all__'
    #  here instead of showing all the fields in the post model  we can do it manually like that :
    # fields = ('title', 'body')



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'
    
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



def LikeView(request, pk):
    post =get_object_or_404(Post, id=request.POST.get('post_id')) # in this line we will get the post_id from the request sent from the form, in the form button there is name = 'post_id'
    liked = False 
    if post.likes.filter(id=request.user.id).exists():
      post.likes.remove(request.user)
      liked = False
    else:
        post.likes.add(request.user)
        liked = True  

    return HttpResponseRedirect(reverse('postdetails', args=[str(pk)]))
