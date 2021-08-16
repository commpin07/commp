from django import template
from django.core import paginator
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Itemfreecon, Comment
from .forms import EditForm, CommentForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q 
from django.db.models import F


# Create your views here.

def indexfreecon(request):
	item_list = Itemfreecon.objects.all().order_by('-id')
	p = Paginator(item_list, 9)
	page = request.GET.get('page')
	item_list = p.get_page(page)
	user = request.user
	context= {
		'item_list':item_list,
		'user': user,
	}
	return render(request, 'freecon/index.html', context)
	
	

# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context ={
#         'item':item,
#     }
#     return render(request, 'contentpiece/detail.html', context) 


class ContentDetail(DetailView):
	model = Itemfreecon
	template_name = 'freecon/detail.html'
	is_favourite = False


# to get context in class based views
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post = context['itemfreecon']
		if post.favre.filter(id=self.request.user.id).exists():
			context['is_favourite'] = True
		return context	


# def create_item(request):
#     form = ItemForm(request.POST, request.FILES)

#     if form.is_valid():
#         form.save()
#         return redirect('contentpiece:index')
#     return render(request, 'contentpiece/item-form.html', {'form':form})  

class CreateItem(CreateView):
    model = Itemfreecon
    fields = ['item_name','item_description','thumbnail', 'article_type', 'item_article', 'article_viewtype','topic', 'language_of_instruction' ]
    template_name = 'freecon/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request,id):
    item = Itemfreecon.objects.get(id=id)
    form = EditForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('freecon:index')
    return render(request, 'freecon/item-form.html', {'form':form, 'item':item})  

def delete_item(request, id):
    item = Itemfreecon.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('freecon:index')

    return render(request, 'freecon/item-delete.html', {'item':item})  

# To display article items in various genres such as video(play_image), pdf, image(play_pic)
def video(request,id):
	item = Itemfreecon.objects.get(id=id)
	item.item_viewcount = F('item_viewcount') + 1
	item.save()

	if item.article_viewtype.id == 1:
		return render(request, 'freecon/play_image.html',{'item':item})
	

# to bookmark

def post_favourite_list(request):
	user = request.user
	favourite_posts = user.favre.all().order_by('-id')
	context = {
		'favourite_posts':favourite_posts
	}
	return render(request, 'freecon/post_favourite_list.html', context)


@login_required
def favourite_post(request, id):
    post = get_object_or_404(Itemfreecon, id=id)
    if post.favre.filter(id=request.user.id).exists():
        post.favre.remove(request.user)
    else:
        post.favre.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())  

	
# Comment Section

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'freecon/add_comment.html'
	def form_valid(self,form):
		form.instance.post_id = self.kwargs['id']
		return super().form_valid(form)
	success_url = reverse_lazy('freecon:indexfreecon')
	
# search function

def search_item(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Itemfreecon.objects.order_by('-id').filter(Q(item_description__icontains=keyword) | Q(item_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'freecon/search_item.html', context)



    



