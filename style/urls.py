from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('styles/', StyleListAPIView.as_view(), name='styles'),
    path('style/<slug:slug>', StyleAPIDetailView.as_view(), name='style'),
    path('profile/<str:username>', UserApiView.as_view(), name='profile'),
    path('items/', ItemAPIView.as_view()),
]