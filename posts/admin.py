from django.contrib import admin


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at']
    search_fields = ['title', 'content', 'created_by']
