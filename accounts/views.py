from django.shortcuts import render,redirect
from .form import RegisteratioinForm  
from . models import Accounts , UserProfile  
from django.contrib import messages,auth
from django.http import HttpResponse

# user verification 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage



def register(request):
    if request.method == 'POST':
        form = RegisteratioinForm(request.POST)  
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            
            # now create user object 
            user = Accounts.objects.create_user(first_name=first_name,last_name=last_name,username=username,email = email,password=password)
            user.phone_number = phone_number
            user.save()
            if user is None:
                messages.error(request,'user creatioin failed')
            
            
            # # make userProfile 
            # profile = UserProfile()
            # profile.user_id = user.id
            # profile.profile_picture = 'default/default-user.png'
            # profile.save()

             # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            print('before')
            send_email.send()
            print('after')
    else:
        form = RegisteratioinForm()                

    context = {
        'form': form,                            
    }
    
    
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email,password=password)
        if user is not None:
        # if user is available then make the user login
            auth.login(request,user)
            messages.success(request,"login successful")
            return redirect('store')
        else:
            messages.error(request,"login failed")
            return redirect('home')
            
    return render(request, 'accounts/login.html', )


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Accounts._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Accounts.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')
