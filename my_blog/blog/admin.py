from django.contrib import admin
from .models import BlogPost

# Customize the BlogPost display in the admin panel
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date')
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'content')

# Register the BlogPost model with the customized admin class
admin.site.register(BlogPost, BlogPostAdmin)
