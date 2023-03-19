from django.urls import path

from tag.views import TagAddAPIView, TagListAPIView, TagRetrieveUpdateDestroyView

app_name = 'tag'


urlpatterns = [
    path('/add', TagAddAPIView.as_view(), name='tag-add'),
    path('/change/<int:pk>', TagRetrieveUpdateDestroyView.as_view(), name='tag-retrive-update-destroy'),
    path('/', TagListAPIView.as_view(), name='tag-list'),

]
