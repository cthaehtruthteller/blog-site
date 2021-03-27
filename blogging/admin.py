from django.contrib import admin
from blogging.models import Post, Category

class CategoriesInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    """designate a category for a post"""
    inlines = [
        CategoriesInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
