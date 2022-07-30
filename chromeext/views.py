from email.mime import text
from django.http.response import HttpResponse
from django.http import  HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Destination
from .forms import ImageForm
from chromeext.models import Destination
from django.conf import settings
from PIL import Image
from pytesseract import pytesseract
import numpy as np
import sys
import string
import re
sys.path.append('../')
# Create your views here.
# Create your views here. 
def home_view(request):
    texts=[]
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            #converter(img_obj.img.url)
            texts=texter(img_obj.img.url)  
            #texter(img_obj.img.url)

            return render(request, 'home.html', {'form': ImageForm(), 'img_obj': img_obj, 'texts':texts})
    else:
          form= ImageForm()
          return render(request, 'home.html', {'form': form})
    
    
def converter(image):
    # Removing that '/' at the beginning of the URL
    url = image[1:]
    imgconv = Image.open(url)
    w,h=imgconv.size
    for i in range(w):
        for j in range(h):
            r,g,b=imgconv.getpixel((i,j))
            r=255-r
            g=255-g
            b=255-b
            imgconv.putpixel((i,j),(r,g,b))

    imgconv.save(url)
 

def texter(image):
    url= image[1:]
    imgc = Image.open(url)
    pytesseract.tesseract_cmd = (r"C:\Users\srija\projects\mychrome\Tesseract-OCR\tesseract.exe")
    text = pytesseract.image_to_string(imgc)  
    return text 
    
    