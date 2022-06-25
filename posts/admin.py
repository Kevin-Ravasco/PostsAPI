from django.contrib import admin
from django.template.defaultfilters import truncatechars


class PostsAdmin(admin.ModelAdmin):
    list_display = ['short_description', 'created_by', 'created_at']
    search_fields = ['content', 'created_by']

    @property
    def short_description(self):
        return truncatechars(self.content, 20)
