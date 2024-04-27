from django.urls import path
from Video_Management import views

# app_name="Video_Management"
urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('mask_feed', views.mask_feed, name='mask_feed'),
    path('livecam_feed', views.livecam_feed, name='livecam_feed'),
]