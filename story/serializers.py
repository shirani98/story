from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from rest_framework import serializers

from category.serializers import CategorySerializer
from comment.models import Comment
from comment.serializers import CommentSerializer
from tag.serializers import TagSerializer

from .models import Story


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'body', 'slug')

class StorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.alias')
    chapters = ChapterSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ('created_at', 'modified_date','slug','user',)

class StoryDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.alias')
    chapters = ChapterSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ('created_at', 'modified_date','slug','user',)

    def get_comments(self, obj):
        comments = Comment.objects.filter(story=obj)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


class StoryCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'
        read_only_fields = ('created_at', 'modified_date','slug','user',)

    def validate_body(self, value):
        if strip_tags(value) != value:
            raise serializers.ValidationError("Story body should not contain HTML tags.")
        return value
