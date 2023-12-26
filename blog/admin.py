from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Comment

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    
admin.site.register(Category, CategoryAdmin)
