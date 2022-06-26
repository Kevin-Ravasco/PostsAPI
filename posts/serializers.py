from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from .models import Post

LIKE = 'LIKE'
UNLIKE = 'UNLIKE'

LIKE_ACTIONS = (
    (LIKE, 'LIKE'),
    (UNLIKE, 'UNLIKE'),
)


class PostSerializer(serializers.ModelSerializer):
    has_liked = serializers.BooleanField(required=False, read_only=True,
                                         help_text='If the logged in user has liked the post')
    like_action = serializers.ChoiceField(choices=LIKE_ACTIONS,
                                          required=False,
                                          write_only=True,
                                          help_text="Supply this field to trigger the like unlike action."
                                                    " Leave it out if no like/unlike action is taken.")

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'likes_count', 'has_liked', 'like_action']
        extra_kwargs = {
            'created_by': {'read_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # remove the like_action field on the docs create view
        if not self.instance:
            self.fields.pop('like_action')

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

    def update(self, instance, validated_data):
        # we validate that the user updating is the creator
        logged_in_user = self.context['request'].user
        like_action = validated_data.get('like_action', None)
        if not logged_in_user == instance.created_by:
            raise PermissionDenied(detail={'error': 'You are not allowed to update this post'},
                                   code='invalid owner')

        instance = super(PostSerializer, self).update(instance, validated_data)

        # To handle the like and unlike actions
        if like_action:
            post_likes = instance.likes
            if like_action == LIKE:
                if logged_in_user.id not in post_likes:
                    post_likes.append(logged_in_user.id)
                    instance.likes = post_likes
            elif like_action == UNLIKE:
                if logged_in_user.id in post_likes:
                    post_likes.remove(logged_in_user.id)
                    instance.likes = post_likes
            instance.save()
        return instance
