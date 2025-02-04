from django import forms
from .models import Post,Category
#choice = [('coding','coding'),('sports','sports'),('entertainement','entertainement')] #if we want to hard codethe list directly 
choice = Category.objects.all().values_list('name','name')   # here we grub the list from the database 

choices_list =[]
for item in choice:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category','body')

        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'this is a title '}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'', 'id':'logged_user', 'type':'hidden'}),
             #'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }
class EditForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'title_tag','body')

        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'this is a title '}),
            'title_tag' : forms.TextInput(attrs={'class=':'form-control'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }        