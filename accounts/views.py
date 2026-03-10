from django.shortcuts import render
from .form import RegisteratioinForm  
from . models import Accounts , UserProfile  
from django.contrib import messages
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

            
    else:
        form = RegisteratioinForm()                

    context = {
        'form': form,                            
    }
    
    
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html', )

