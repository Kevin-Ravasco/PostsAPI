from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    has_liked = serializers.BooleanField(required=False, read_only=True)  # if the logged-in user has liked the post

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'likes_count', 'has_liked']
        extra_kwargs = {
            'created_by': {'read_only': True}
        }

    def to_representation(self, instance):
        user_id = self.context['request'].user.id
        data = super(PostSerializer, self).to_representation(instance)
        data['has_liked'] = user_id in instance.likes
        return data

    def create(self, validated_data):
        """
        We override the create method to make the post
        object to be created by the currently logged-in user.
        """
        post = Post(**validated_data)
        post.created_by = self.context['request'].user
        post.save()
        return post
