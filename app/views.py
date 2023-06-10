from django.shortcuts import render

# Create your views here.

def mdb_jquery(request):
    return render(request,'mdb_jquery.html')

def bg_image(request):
    return render(request,'bg_image.html')