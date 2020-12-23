from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'slug', 'publish']
    search_fields = ['title', 'body']
    list_filter = ['status', 'publish']
    prepopulated_fields = {'slug': ('title', 'body',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', '-publish']


admin.site.register(Post, PostAdmin)
