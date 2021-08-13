from django.urls import path
from . import views


app_name = 'myapp'
urlpatterns= [
    # resources link
    path('', views.action, name='action'),
   

]
