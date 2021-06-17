from django import template
from django.core import paginator
from django.db.models.query import prefetch_related_objects
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from flashcard.models import ItemFC, CommentFlashCard
from .forms import CommentForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.db.models import Q 
from django.contrib.auth.decorators import login_required


# Create your views here.

# flashcard index page
def index(request):
	item_list = ItemFC.objects.all().order_by('-id')
	p = Paginator(item_list, 9)
	page = request.GET.get('page')
	item_list = p.get_page(page)
	user = request.user
	context= {
		'item_list':item_list,
		'user': user,
	}
	return render(request, 'flashcard/index.html', context)
	
# details page	
class ContentDetail(DetailView):
	model = ItemFC
	template_name = 'flashcard/detail.html'
	is_favourite = False


# to get context in class based views
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post = context['itemfc']
		if post.fav.filter(id=self.request.user.id).exists():
			context['is_favourite'] = True
		return context	

# to show flashcard
def video(request,id):
	item = ItemFC.objects.get(id=id)

	if item.article_viewtype.id == 1:
		return render(request, 'flashcard/play_pic.html',{'item':item})	

# to add comments
class AddCommentView(CreateView):
	model = CommentFlashCard
	form_class = CommentForm
	template_name = 'flashcard/add_comment.html'
	def form_valid(self,form):
		form.instance.post_id = self.kwargs['id']
		return super().form_valid(form)
	success_url = reverse_lazy('flashcard:index')        

# to bookmark

def posts_favourite_list(request):
	user = request.user
	favourite_posts = user.fav.all()
	context = {
		'favourite_posts':favourite_posts
	}
	return render(request, 'flashcard/post_favourite_list.html', context)


@login_required
def favourite_posts(request, id):
    post = get_object_or_404(ItemFC, id=id)
    if post.fav.filter(id=request.user.id).exists():
        post.fav.remove(request.user)
    else:
        post.fav.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())  
