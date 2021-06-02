from django.urls import path
from . import views


app_name = 'myposts'
urlpatterns= [
    # resources link
    path('', views.index, name='index'),

    # detail view
    path('<int:pk>/',views.ContentDetail.as_view(), name='detail'),

    # adding item
    path('add/',views.CreateItem.as_view(), name='create_item'),

    # edit item
    path('update/<int:id>/', views.update_item, name='update_item'),

    # delete item
    path('delete/<int:id>', views.delete_item, name='delete'),
]