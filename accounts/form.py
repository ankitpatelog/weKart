from django import forms
from . models import Accounts,UserProfile

class RegisteratioinForm(forms.ModelForm):
    # generate password field 
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter your password',
        'class' : 'form-control',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter your password',
        'class' : 'form-control',
    }))
    
    class Meta:
        model = Accounts
        fields = ['first_name','last_name','phone_number','email']
        
    # initialize the function that add the widget when the field made 
    def __inti__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget_attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget_attrs['placeholder'] = 'Enter your last name'
        self.fields['phone_number'].widget_attrs['placeholder'] = 'Enter your phone_number'
        self.fields['email'].widget_attrs['placeholder'] = 'Enter your email'
        
        for field in self.fields:
            self.fields[field].widget_attrs['class'] = 'form-control'
            
            
    # handle form different passwrod error
    def clean(self):
        cleaned_data = super().clean()
        # same email error
        # email = cleaned_data.get('email')
        
        # is_email_exist = Accounts.objects.filter(email=email).isexist()
        # if is_email_exist == False:
        #     raise forms.ValidationError(
        #         "Email already exists"
        #     )
        
        # handle different pass error
        password = cleaned_data.get('password') 
        confirm_password = cleaned_data.get('confirm_password') 
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Both password does not match"
            )

            
class UserForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget_attrs['class'] = 'form-control'
            

# userprofile form
class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'