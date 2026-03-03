from django.contrib import admin
from . models import Accounts
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# change the Accounts field to show into the admin page
class AccountAdmin(UserAdmin):
    list_display = ('email','username' ,'first_name','last_name', 'last_login' , 'date_joined','is_active')
    list_display_links = ('email','username')
    
    fieldsets = () # make the password unreadable into the admin page
    
    # list_filter = ('email','username','is_active') use to filter values in the right side
    filter_horizontal = ()
    readonly_fields = ('last_login', 'date_joined') # make the values not in editable form and direcly diaplay the values




admin.site.register(Accounts,AccountAdmin)


