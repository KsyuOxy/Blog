from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'timestamp', 'updated', 'draft']
    list_display_links = ['author', 'timestamp']
    list_editable = ['title']

    list_filter = ['title', 'author', 'timestamp', 'updated']
    search_fields = ['author__username', 'title']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
