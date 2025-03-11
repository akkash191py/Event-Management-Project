from django.contrib import admin
from UserAccount.models import User
# Register your models here.
# BankDetails Model register
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'mobile', 'role','date_joined', 'created_at')
    list_filter = ('role', 'is_staff', 'is_active', 'is_admin', "is_superuser")
    search_fields = ('first_name', 'last_name', 'role', 'email', 'id')
    
admin.site.register(User, UserAdmin)