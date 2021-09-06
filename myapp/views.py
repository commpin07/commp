
from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemVid, Comreview
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    
    return render(request, 'home.html')

def action(request):
    item = ItemVid.objects.get()
    return render(request, 'myapp/action.html',{'item':item})

def reviewss(request):
    item_list = Comreview.objects.all().order_by('-id')
    p = Paginator(item_list, 9)
    page = request.GET.get('page')
    item_list = p.get_page(page)
    user = request.user
    context= {
		'item_list':item_list,
		'user': user,
	}
    return render(request, 'myapp/reviews.html', context)