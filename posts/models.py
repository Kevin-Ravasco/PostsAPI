from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = ArrayField(base_field=models.PositiveIntegerField(), default=list, db_index=True)

    def __str__(self):
        return f'Post by {self.created_by}'

    @property
    def likes_count(self):
        return len(self.likes)
