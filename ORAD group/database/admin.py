from django.contrib import admin
from .models import CustomUser, Document

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=["email", "first_name", "last_name", "is_active", "is_staff", "date_joined"]
    search_fields = ["email", "first_name", "last_name"]
    list_filter = ['is_active', 'is_staff']
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploader', 'file', 'uploaded_at']  # Fields to display in the admin list view
    search_fields = ['title']  # Fields to enable search functionality in the admin interface
    list_filter = ['uploader', 'uploaded_at']  # Fields to filter results in the admin interface
