from django.urls import path

from comment.views import (
    CommentCreateAPIView,
    CommentListAdminAPIView,
    CommentListAPIView,
    CommentRetrieveUpdateDestroyAPIView,
    UserCommentListAPIView,
)

app_name = 'comment'
urlpatterns = [
    path('/list/', CommentListAdminAPIView.as_view(),name='comment-admin-list'),
    path('/story-comment/<slug:storyslug>/', CommentListAPIView.as_view(),name='comment-list'),
    path('/add/<slug:storyslug>/', CommentCreateAPIView.as_view() ,name='comment-create'),
    path('/change/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(),name='comment-detail'),
    path('/user-comment/', UserCommentListAPIView.as_view(),name='user-comment-list'),
]
