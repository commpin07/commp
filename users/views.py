from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from contentpiece.models import Item
from .models import Profile
from django.http import HttpResponseRedirect, HttpResponse

# password reset 
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError

from django.db.models.query_utils import Q

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form':form})

# def profileEdit(request):
#     # profile = Profile.objects.get(id=id)
  
#     if request.method == 'POST':
#         form = ProfileEditForm(request.POST, request.FILES, instance = request.user)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             form.save()
#             return redirect('login')
#     else:
#         form = ProfileEditForm()
#     return render(request, 'users/profile_edit.html', {'form':form})



@login_required
def profilepage(request):
    return render(request, 'users/profile.html')   

# forgot password

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('users/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'users/forgotPassword.html')    


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(id=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'users/resetPassword.html' )       
