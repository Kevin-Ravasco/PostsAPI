from django.contrib import admin


class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at']
    search_fields = ['content', 'created_by']
