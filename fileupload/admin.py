from django.contrib import admin
from .models import Files


@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('file', 'id')
    date_hierarchy = 'uploaded_at'
