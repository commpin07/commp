from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'dtt'
urlpatterns = [
    path('', views.index, name='index'),

    # path('<int:pk>/', login_required(views.ContentDetail.as_view()), name='detail'),

    path('update/<int:id>/', views.update_item, name='update_item'),

    # path('<int:pk>/feedback/', views.ContentFeedback.as_view(), name='feedback'),
    path('<int:id>/feedback/', views.feedback, name='feedback'),

    path('suggestion/', views.suggestions, name='suggestions'),

]