from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('styles/', StyleListAPIView.as_view(), name='style_list'),
    path('style/<slug:slug>', StyleAPIDetailView.as_view(), name='style_detail'),
    path('items/', ItemAPIView.as_view()),
]