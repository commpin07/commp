from django.shortcuts import render
from django.http import HttpResponse
from .models import Expert

from django import template
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render
from django.http import HttpResponse
from contentpiece.models import Item
# from contentpiece.forms import EditForm, ItemForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.core.paginator import Paginator



# Create your views here.

def expertView(request):
    expert = Expert.objects.all()
    return render(request,'expert/expertView.html', {'expert':expert})

def index(request,id):
    expert_name = Expert.objects.filter(id=id)
    # user = User.objects.filter(id=id)
    # item_list = Item.objects.filter(user_name=id).order_by('-id')
    # p = Paginator(item_list, 9)
    # page = request.GET.get('page')
    # item_list = p.get_page(page)
    # if len(item_list) == 0:
    #     return render(request, 'expert/sorry.html', {'item_list':item_list})
    # else:
    #     return render(request, 'expert/exprt_index.html', {'item_list':item_list})
    print(expert_name)
    return HttpResponse("I love Tanya Singh")
    

class ContentDetail(DetailView):
    model = Item
    template_name = 'expert/detail.html'    
