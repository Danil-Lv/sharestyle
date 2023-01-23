from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView

from profiles.models import User
from profiles.serializers import UserSerializer
from style.permissions import IsOwnerOrReadOnly


# Create your views here.
class UserApiView(RetrieveUpdateAPIView):
    """Вывод/изменение профиля пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = 'username'