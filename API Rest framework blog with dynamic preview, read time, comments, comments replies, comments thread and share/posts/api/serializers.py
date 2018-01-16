from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    )

from posts.models import Post
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from accounts.api.serializers import UserDetailSerializer


post_detail_url = HyperlinkedIdentityField(
        view_name='posts_api:detail',
        lookup_field='slug',
    )


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    edit_url = HyperlinkedIdentityField(
        view_name='posts_api:update',
        lookup_field='slug',
    )
    delete_url = HyperlinkedIdentityField(
        view_name='posts_api:delete',
        lookup_field='slug',
    )
    # user = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)
    image2 = SerializerMethodField()
    html = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'edit_url',
            'delete_url',
            'title',
            'slug',
            'content',
            'html',
            'user',
            'image',
            'image2',
            'added',
            'updated',
            'publish',
            'draft',
            'read_time',
            'height_field',
            'width_field',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image2(self, obj):
        try:
            image2 = obj.image.url
            # image2 = obj.image.path
        except:
            # image2 = None
            image2 = 'no image here'
        return image2

    def get_html(self, obj):
        return obj.get_markdown()


class PostDetailSerializer(ModelSerializer):
    # user = SerializerMethodField()
    user = UserDetailSerializer(read_only=True)
    image2 = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'html',
            'user',
            'image',
            'image2',
            'added',
            'updated',
            'publish',
            'draft',
            'read_time',
            'height_field',
            'width_field',
            'comments',
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image2(self, obj):
        try:
            image2 = obj.image.url
            # image2 = obj.image.path
        except:
            # image2 = None
            image2 = 'no image here'
        return image2

    def get_html(self, obj):
        return obj.get_markdown()

    def get_comments(self, obj):
        comments_qs = Comment.objects.filter_by_queryset(obj)
        comments = CommentSerializer(comments_qs, many=True).data
        return comments


class PostCreateSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'user',
            'image',
            'publish',
            'draft',
        ]


class PostUpdateSerializer(ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'user',
            'image',
            'updated',
            'publish',
            'draft',
        ]

