from django import forms
from .models import Post,Data




class ArtcalsForm(forms.ModelForm):
    title=forms.CharField(widget = forms.TextInput(attrs={
            "name": "title",
            "type": "text",
            "class": "form-control  inline",
            "placeholder":"Example input",
            
        }), label = "title")
    class Meta:
        model = Post
        fields = ['title']



class ImagesForm(forms.ModelForm):
    
    name_file = forms.FileField(widget = forms.TextInput(attrs={
            "name": "images",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
        }), label = "")
    class Meta:
        model = Data
        fields = ['name_file']