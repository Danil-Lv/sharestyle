from django.urls import path, include
from .views import *

urlpatterns = [
    path('<str:username>/', UserApiView.as_view(), name='user_detail'),
    path('follow/<str:username>/', FollowersApiView.as_view()),
    path('unfollow/<str:username>/', UnfollowApiView.as_view())

]