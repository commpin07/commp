from django.urls import path
from . import views


app_name = 'freecon'
urlpatterns= [
    # resources link
    path('', views.indexfreecon, name='indexfreecon'),


    # detail view
    path('<int:pk>/',views.ContentDetail.as_view(), name='detail'),

    # adding item
    # path('add/',views.CreateItem.as_view(), name='create_item'),

    # edit item
    # path('update/<int:id>/', views.update_item, name='update_item'),

    # delete item
    # path('delete/<int:id>', views.delete_item, name='delete'),

    # to display article items
    path('video/<int:id>', views.video, name='play_image'),

    

    # to bookmark
    path('favourite/<int:id>', views.favourite_post, name='favourite_post'), 
    path('favourites/', views.post_favourite_list, name='post_favourite_list'),

    # to comment
    path('<int:id>/comment', views.AddCommentView.as_view(), name='add_comment'),

    # search bar
    path('search/',views.search_item, name='search_item'),

    

    

    
   

]
