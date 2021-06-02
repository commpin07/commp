from django import template
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render
from django.http import HttpResponse
from contentpiece.models import Item
from contentpiece.forms import EditForm, ItemForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.core.paginator import Paginator



# Create your views here.


def index(request):
    item_list = Item.objects.filter(user_name=request.user).order_by('-id')
    p = Paginator(item_list, 9)
    page = request.GET.get('page')
    item_list = p.get_page(page)
    if len(item_list) == 0:
        return render(request, 'myposts/sorry.html', {'item_list':item_list})
    else:
        return render(request, 'myposts/index.html', {'item_list':item_list})


# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context ={
#         'item':item,
#     }
#     return render(request, 'contentpiece/detail.html', context) 

class ContentDetail(DetailView):
    model = Item
    template_name = 'myposts/detail.html'    

# def create_item(request):
#     form = ItemForm(request.POST, request.FILES)

#     if form.is_valid():
#         form.save()
#         return redirect('contentpiece:index')
#     return render(request, 'contentpiece/item-form.html', {'form':form})  

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_description','thumbnail', 'item_article', 'article_type', 'topic' ]
    template_name = 'myposts/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = EditForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('myposts:index')
    return render(request, 'myposts/item-form.html', {'form':form, 'item':item})  

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('myposts:index')

    return render(request, 'myposts/item-delete.html', {'item':item})  

