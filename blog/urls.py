from django.urls import path
from . import views


app_name = 'blog'
urlpatterns= [
    # resources link
    path('', views.indexblg, name='indexblg'),


    # detail view
    path('<int:pk>/',views.ContentDetail.as_view(), name='detail'),


    # to display article items
    path('video/<int:id>', views.video, name='play_pdf'),

    # adding item
    # path('add/',views.create_item, name='create_item'),

    # to bookmark
    path('favourite/<int:id>', views.favourite_posts, name='favourite_posts'), 
    path('favourites/', views.posts_favourite_list, name='posts_favourite_list'),

    # to comment
    path('<int:id>/comment', views.AddCommentView.as_view(), name='add_comment'),

    # search bar
    path('search/',views.search_item, name='search_item'),
    
]