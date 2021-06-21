from .models import ItemDib, CommentDib
from django import template
from django.core import paginator
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CommentForm, ItemForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.db.models import Q 
from django.contrib.auth.decorators import login_required


# Create your views here.

# flashcard index page
def index(request):
	item_list = ItemDib.objects.all().order_by('-id')
	p = Paginator(item_list, 9)
	page = request.GET.get('page')
	item_list = p.get_page(page)
	user = request.user
	context= {
		'item_list':item_list,
		'user': user,
	}
	return render(request, 'disboard/index.html', context)

class ContentDetail(DetailView):
	model = ItemDib
	template_name = 'disboard/detail.html'
	is_favourite = False


# to get context in class based views
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post = context['itemdib']
		if post.favs.filter(id=self.request.user.id).exists():
			context['is_favourite'] = True
		return context	    


# start new discussion
def create_item(request):
    form = ItemForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('disboard:index')
    return render(request, 'disboard/item-form.html', {'form':form})  


# to add comments
class AddCommentView(CreateView):
	model = CommentDib
	form_class = CommentForm
	template_name = 'disboard/add_comment.html'
	def form_valid(self,form):
		form.instance.post_id = self.kwargs['id']
		return super().form_valid(form)
	success_url = reverse_lazy('disboard:index')    


# to bookmark

def posts_favourite_list(request):
	user = request.user
	favourite_posts = user.favs.all().order_by('-id')
	context = {
		'favourite_posts':favourite_posts
	}
	return render(request, 'disboard/post_favourite_list.html', context)


@login_required
def favourite_posts(request, id):
    post = get_object_or_404(ItemDib, id=id)
    if post.favs.filter(id=request.user.id).exists():
        post.favs.remove(request.user)
    else:
        post.favs.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())  


# search bar
def search_item(request):
    if 'keywords' in request.GET:
        keyword = request.GET['keywords']
        if keyword:
            products = ItemDib.objects.order_by('-id').filter(Q(description__icontains=keyword) | Q(item_title__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'disboard/search_item.html', context)
    
