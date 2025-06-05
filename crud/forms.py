from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from typing import Any
from django import forms
from .models import post



class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields["text"].label = ""
            # self.fields["password"].label = ""
            
    class Meta:
        model=post
        fields=["text"]
        widgets={
                    'text':forms.Textarea(attrs={"rows":"4", "cols":"50","placeholder":"..."}),
                
                }



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

   