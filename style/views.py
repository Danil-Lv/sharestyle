from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import permissions
from rest_framework.viewsets import ViewSet

from .models import Style, Item, Review
from .permissions import IsOwnerOrReadOnly
from .serializers import StyleSerializer, ItemSerializer, ReviewCreateSerializer
from .service import StyleFilter

from django_filters.rest_framework import DjangoFilterBackend



class StyleListAPIView(ListCreateAPIView):
    """Вывод/создание  стилей"""

    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StyleFilter

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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ReviewAPIView(CreateAPIView):
    """Создание комментариев"""
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
