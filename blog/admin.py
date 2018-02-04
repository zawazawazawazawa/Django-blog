from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
