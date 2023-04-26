from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','company_name','company_website', 'company_address', 'city', 'state', 'zip_code', 'country']
