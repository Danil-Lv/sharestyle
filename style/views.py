from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import permissions

from .models import Style, Item
from .permissions import IsOwnerOrReadOnly
from .serializers import StyleSerializer, ItemSerializer


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


class ItemAPIView(ListCreateAPIView):
    """Вывод/создание вещей"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
