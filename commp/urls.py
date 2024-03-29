"""commp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from commp.myapp.views import action
from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from myapp import views as myapp_views

from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/',include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),

    # home page
    # path('',myapp_views.home, name='home'),
    # path('action',myapp_views.action, name='action'),
    path('action/', include('myapp.urls')),

    # contentpiece app
    path('featured/', include('contentpiece.urls')),

    path('conversations/', include('freecon.urls')),

    
    
    # user registration
    path('register/',users_views.register, name='register'),

    # login
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # logout
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # profile page
    path('profile/',users_views.profilepage, name='profile'),

    
    # flashcards
    path('flashcard/',include('flashcard.urls')),

    # blog
    path('blog/',include('blog.urls')),

    # decision tree
    path('dt/', include('dtt.urls')),

    # sean 
    path('',include('sean.urls')),

    

    # forgot password
    path('forgotPassword/', users_views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', users_views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', users_views.resetPassword, name='resetPassword'),

    
    # myposts
    path('myposts/', include('myposts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
