from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin, IsAuth
from story.models import Story

from .models import Comment
from .serializers import CommentSerializer


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        try:
            story = Story.objects.get(slug=self.kwargs['storyslug'])
        except Exception:
            raise ValidationError('Invalid story slug provided.')
        queryset = Comment.objects.filter(story=story)
        return queryset

class CommentListAdminAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('-created_at')
    permission_classes = [IsAdmin]
    pagination_class = PageNumberPagination


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuth]

    def perform_create(self, serializer):
        try:
            story_slug = self.kwargs['storyslug']
            story = Story.objects.get(slug=story_slug)
            serializer.save(user=self.request.user, story=story)
        except Story.DoesNotExist:
            raise ValidationError('Invalid story slug provided.')
        except KeyError:
            raise ValidationError('Story slug is missing from URL.')

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuth]


class UserCommentListAPIView(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        user_comments = Comment.objects.filter(user=request.user).order_by('-created_at')
        serializer = CommentSerializer(user_comments, many=True)
        return Response(serializer.data)
