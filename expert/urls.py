from django.urls import path
from . import views


app_name = 'expert'
urlpatterns= [
    # expert list
    path('',views.expertView, name='expertView'),

    # resources link
    path('<int:id>/', views.index, name='index'),

    # detail view
    path('<int:pk>/',views.ContentDetail.as_view(), name='detail'),

]   