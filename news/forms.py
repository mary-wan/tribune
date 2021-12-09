from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import Textarea
from news import email
from .models import Article

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField(help_text='Required. Enter a valid email address.')
    
    # specify model it will interact with
    class Meta:
        model = User  
        fields= ['username','email','password1','password2']
        
        # help_texts = {
        #     'username': None,
        #     'password1':None,
        #     'password2':None,
            
        #     }


User._meta.get_field('email')._unique = True 

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        # widgets = {
        #     'post': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }