from django.contrib import admin
from .models import Post, Comment, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1                
    fields = ('image',)  

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    inlines = [PostImageInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'created_at')
    search_fields = ('name', 'email', 'body')
    list_filter = ('created_at',)
