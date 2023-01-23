from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import permissions

from .models import Style, User, Item
from .permissions import IsOwnerOrReadOnly
from .serializers import StyleSerializer, UserSerializer, ItemSerializer


# Create your views here.

class StyleListAPIView(ListCreateAPIView):
    """Вывод/создание  стилей"""
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StyleAPIDetailView(RetrieveUpdateDestroyAPIView):
    """Вывод/изменение/удаление одного стиля"""
    lookup_field = 'slug'
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class UserApiView(RetrieveUpdateAPIView):
    """Вывод/изменение профиля пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    lookup_field = 'username'




class ItemAPIView(ListCreateAPIView):
    """Вывод/создание вещей"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
