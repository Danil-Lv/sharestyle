from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Style
from .permissions import IsOwnerOrReadOnly
from .serializers import StyleSerializer
from rest_framework import permissions


# Create your views here.

class StyleListAPIView(ListCreateAPIView):
    """Вывод всех стилей"""
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class StyleAPIDetailView(RetrieveUpdateDestroyAPIView):
    """Вывод одного стиля"""
    lookup_field = 'slug'
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    
