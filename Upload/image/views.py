from django.shortcuts import render,redirect, HttpResponse
import pytesseract
import os
from PIL import Image as IMAGE
# Create your views here.
from .models import Image, Text
from .form import ImageForm, TextF

import cv2 
import pytesseract as pts
import subprocess
def output(extracted_text):
    c_file_name = "output.c"
    # check if file exists 
    #code to delete entire data along with file
    # Open the file in write mode 
    if os.path.exists(c_file_name): 
        os.remove(c_file_name)   
    with open("Upload/output.c", "w") as c_file:
        # Write your C code to the file
        c_file.write(extracted_text)
    #print(f"C file '{c_file_name}' created successfully.")
    subprocess.run(["gcc", "Upload/output.c", "-o", "output"])
    out = subprocess.run(["./output"], capture_output=True, text=True)
    return out.stdout
    
def index(request):
    form=ImageForm()
    #img=Image.objects.all()
    if request.method == "POST":
        form = ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"upload.html",{"form":form,"obj":obj})
    return render(request,"index.html",{"form":form})


#def extract(request):
def extract(request, pk):
    #pk = 58
    print("Inside Extract Function")
    instance = Image.objects.get(pk=pk)
    path = instance.image.path
    extracted_text = pytesseract.image_to_string(IMAGE.open(path))
    #obj.text = extracted_text
    #toText(extracted_text)
    
    #img=Image.objects.all()
    '''print(">>>>>>>>>>",request.method)
    if request.method == "POST":
        form = TextF(data=request.POST)
        print("sfhagag")
        if form.is_valid():
            print("Hello")
            form.save()
            obj=form.instance
            #extracted_text=obj.text
            result = output(extracted_text)
            return redirect(request,'out.html',{"result":result})
        else:
            print("world")
            return HttpResponse("invalid")'''
    form = TextF()
    return render(request, 'c_file.html',{"text":extracted_text,"instance":instance,"form":form})

def extracting(request):
    print(">>>>>>>>>>",request.method)
    if request.method == "POST":
        form = TextF(data=request.POST)
        print("sfhagag")
        if form.is_valid():
            print("Hello")
            form.save()
            obj=form.instance
            extracted_text=obj.text
            result = output(extracted_text)
            return render(request,'out.html',{"result":result})
        else:
            print("world")
            return HttpResponse("invalid")
        

def delete(request,pk):
    instance = Image.objects.get(pk=pk)
    instance.delete()
    form=ImageForm()
    img=Image.objects.all()
    return render(request,"index.html",{"form":form,"img":img})


def out(request):
    return HttpResponse("nfvdvb")