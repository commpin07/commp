from django import template
from django.core import paginator
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Like, Comment
from .forms import EditForm, ItemForm, CommentForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Q 
from django.db.models import F


# Create your views here.

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
	return render(request, 'contentpiece/index.html', context)
	
	

# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context ={
#         'item':item,
#     }
#     return render(request, 'contentpiece/detail.html', context) 


class ContentDetail(DetailView):
	model = Item
	template_name = 'contentpiece/detail.html'
	is_favourite = False


# to get context in class based views
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post = context['item']
		if post.favourite.filter(id=self.request.user.id).exists():
			context['is_favourite'] = True
		return context	


# def create_item(request):
#     form = ItemForm(request.POST, request.FILES)

#     if form.is_valid():
#         form.save()
#         return redirect('contentpiece:index')
#     return render(request, 'contentpiece/item-form.html', {'form':form})  

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_description','thumbnail', 'article_type', 'item_article', 'article_viewtype','topic', 'language_of_instruction' ]
    template_name = 'contentpiece/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request,id):
    item = Item.objects.get(id=id)
    form = EditForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('contentpiece:index')
    return render(request, 'contentpiece/item-form.html', {'form':form, 'item':item})  

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('contentpiece:index')

    return render(request, 'contentpiece/item-delete.html', {'item':item})  

# To display article items in various genres such as video(play_image), pdf, image(play_pic)
def video(request,id):
	item = Item.objects.get(id=id)
	item.item_viewcount = F('item_viewcount') + 1
	item.save()

	if item.article_viewtype.id == 1:
		return render(request, 'contentpiece/play_image.html',{'item':item})

	if item.article_viewtype.id == 2:
		return render(request, 'contentpiece/play_pdf.html',{'item':item})

	if item.article_viewtype.id == 3:
		return render(request, 'contentpiece/play_pic.html',{'item':item})	

# to like/dislike posts
def post_like(request):
	user = request.user
	if request.method == "POST":
		post_id = request.POST.get('post_id')
		post_obj = Item.objects.get(id=post_id)
		if user in post_obj.liked.all():
			post_obj.liked.remove(user)
		else:
			post_obj.liked.add(user)

		like, created = Like.objects.get_or_create(user=user, post_id=post_id)

		if not created:
			if like.value == 'Like':
				like.value = 'Unlike'
			else:
				like.value = 'Like'
		like.save()				
	return redirect('contentpiece:index')

# to bookmark

def post_favourite_list(request):
	user = request.user
	favourite_posts = user.favourite.all().order_by('-id')
	context = {
		'favourite_posts':favourite_posts
	}
	return render(request, 'contentpiece/post_favourite_list.html', context)


@login_required
def favourite_post(request, id):
    post = get_object_or_404(Item, id=id)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())  

	
# Comment Section

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'contentpiece/add_comment.html'
	def form_valid(self,form):
		form.instance.post_id = self.kwargs['id']
		return super().form_valid(form)
	success_url = reverse_lazy('contentpiece:index')
	
# search function

def search_item(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Item.objects.order_by('-id').filter(Q(item_description__icontains=keyword) | Q(item_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'contentpiece/search_item.html', context)


def about(request):
	return render(request, 'contentpiece/about.html')	
    


