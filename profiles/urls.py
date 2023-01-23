from django.urls import path, include
from .views import *

urlpatterns = [
    path('<str:username>/', UserApiView.as_view(), name='profile'),
]