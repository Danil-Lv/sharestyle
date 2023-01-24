from rest_framework import permissions, response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView

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


class FollowersApiView(APIView):
    """Подписка на пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user = User.objects.filter(username=username)
        if user.exists():
            user[0].subscribers.add(request.user)
            return response.Response(status=201)
        return response.Response(status=404)


class UnfollowApiView(APIView):
    """Отписка от пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user = User.objects.filter(username=username)
        if user.exists():
            user[0].subscribers.remove(request.user)
            return response.Response(status=201)
        return response.Response(status=404)




