from django import forms 
from chromeext.models import Destination
  

    

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Destination
        fields = ['id', 'img']
