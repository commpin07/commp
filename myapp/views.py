
from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemVid

# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def action(request):
    item = ItemVid.objects.get()
    return render(request, 'myapp/action.html',{'item':item})

def reviewss(request):
    return render(request, 'myapp/reviews.html')    