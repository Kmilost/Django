from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def page1(request):
    return render(request,'core/page1.html')