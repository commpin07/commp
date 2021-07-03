from django.shortcuts import render, redirect

from .models import Item
from django.views.generic.detail import DetailView
from .forms import ItemAnswerForm, SuggestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

count = 1

def index(request):
    item_list = Item.objects.all().order_by('-id')
    p = Paginator(item_list, 9)
    page = request.GET.get('page')
    item_list = p.get_page(page)
    user = request.user
    context= {
		'item_list':item_list,
		'user': user,
	}
    return render(request, 'dtt/index.html', context)
    

class ContentDetail(DetailView):
       model = Item
       template_name = 'dtt/detail.html'


# class ContentFeedback(DetailView):
#     model = Item
#     template_name = 'dtt/feedback.html'    

def feedback(request,id):
    item = Item.objects.get(id=id)
    if item.answer == "option 1":
        return render(request, 'dtt/feedback1.html',{'item':item})
    if item.answer == "option 2":
        return render(request, 'dtt/feedback2.html',{'item':item})
    if item.answer == "option 3":
        return render(request, 'dtt/feedback3.html',{'item':item})    
    return render(request, 'dtt/feedback.html', {'item':item})    


@login_required
def update_item(request,id):
    item = Item.objects.get(pk=id)
    form = ItemAnswerForm(request.POST, instance=item)
    global count
    count += 1
    print(count)

    if form.is_valid():
        form.save()
        return redirect('dtt:detail',pk=item.id)
    return render(request, 'dtt/answer_form.html', {'form':form, 'item':item}) 

def suggestions(request):
    
    form = SuggestionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dtt:index')
    return render(request, 'dtt/suggestion_form.html', {'form':form}) 

