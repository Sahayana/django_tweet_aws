# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('tweet/', views.tweet, name='tweet'),
        path('tweet/delete/<int:id>', views.delete_tweet, name='delete_tweet'),
        path('tweet/comment/<int:tweet_id>', views.comment_create, name='comment_create'),
        path('tweet/comment/delete/<int:id>', views.comment_delete, name='comment_delete'),
        path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
        path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]