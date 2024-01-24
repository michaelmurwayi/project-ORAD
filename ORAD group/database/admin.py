from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=["email", "first_name", "last_name", "is_active", "is_staff", "date_joined"]
    search_fields = ["email", "first_name", "last_name"]