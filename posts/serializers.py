from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    has_liked = serializers.BooleanField(required=False, read_only=True)  # if the logged-in user has liked the post

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'likes_count', 'has_liked']

    def to_representation(self, instance):
        user_id = self.context['request'].user.id
        data = super(PostSerializer, self).to_representation(instance)
        data['has_liked'] = user_id in instance.likes
        return data
