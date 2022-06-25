from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

User = get_user_model()


class Post(models.Model):
    content = models.TextField()
    file = models.FileField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = ArrayField(base_field=models.PositiveIntegerField(), db_index=True)

    def __str__(self):
        return f'Post by {self.created_by}'
