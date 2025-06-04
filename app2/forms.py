from django import forms
from .models import Image,Artcals




class ArtcalsForm(forms.ModelForm):
    title=forms.CharField(widget = forms.TextInput(attrs={
            "name": "title",
            "type": "text",
            "class": "form-control  inline",
            "placeholder":"Example input",
            
        }), label = "title")
    class Meta:
        model = Artcals
        fields = ['title']



class ImagesForm(forms.ModelForm):
    
    pic = forms.FileField(widget = forms.TextInput(attrs={
            "name": "images",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
        }), label = "")
    class Meta:
        model = Image
        fields = ['pic']