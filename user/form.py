
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

        
        help_texts = {
            'username': None,
            'email': None,
        }

   
    # def __init__(self, *args, **kwargs):
    #         super(UserCreationForm, self).__init__(*args, **kwargs)
    #         for fieldname in ["username","email","password1","password2"]:
    #             self.fields[fieldname].help_text = None    

   