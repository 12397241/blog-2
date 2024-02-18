from django.contrib import admin
from .models import Post

# Register your models here.
class PostRoy(admin.ModelAdmin):
    list_display = ['title','slug','author','pulish', 'status']
    list_filter = ['status', 'created','publish','author']
    search_fields = ['tetle', 'body']
    preserve_filters = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
