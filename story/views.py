from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin, IsAuth, IsAuthor

from .models import Story
from .serializers import StoryCreatorSerializer, StoryDetailSerializer, StorySerializer


class SearchView(generics.ListAPIView):
    serializer_class = StorySerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        user = self.request.GET.get('user')
        tag = self.request.GET.get('tag')

        if category:
            queryset = Story.objects.filter(categories__name__icontains=category)
        elif user:
            queryset = Story.objects.filter(user__alias__icontains=user)
        elif tag:
            queryset = Story.objects.filter(tags__name__icontains=tag)
        elif query:
            queryset = Story.objects.filter(Q(body__icontains=query) | Q(brief__icontains=query) | Q(user__alias__icontains=query))
        else:
            # return all stories if no search parameters are provided
            queryset = Story.objects.none()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StoryListAPIView(generics.ListAPIView):
    serializer_class = StorySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Story.objects.all()
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(user__username=username)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StoryCreateAPIView(generics.CreateAPIView):
    serializer_class = StoryCreatorSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthor]


class StoryDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    permission_classes = []



class SavedStoriesAPIView(generics.ListAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsAuth]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        return user.saved_stories.all()


class CreateSaveStoryAPIView(APIView):
    permission_classes = [IsAuth]

    def post(self, request,story_slug, *args, **kwargs):
        user = request.user
        try:
            story = Story.objects.get(slug=story_slug)
        except Story.DoesNotExist:
            return Response({'detail': 'Story not found.'})

        user.saved_stories.add(story)
        return Response({'detail': 'Story saved successfully.'})

class DeleteSavedStoryAPIView(generics.DestroyAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsAuth]

    def delete(self, request, *args, **kwargs):
        user = request.user
        story_id = self.kwargs.get('story_slug')
        try:
            story = user.saved_stories.get(slug=story_id)
        except Story.DoesNotExist:
            return Response({'detail': 'Story not found in saved stories.'})

        user.saved_stories.remove(story)
        return Response({'detail': 'Story removed from saved stories successfully.'})
