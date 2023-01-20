from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('styles/', StyleListAPIView.as_view()),
    path('style/<slug:slug>', StyleAPIDetailView.as_view()),

]