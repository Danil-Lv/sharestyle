from rest_framework import serializers
from rest_framework.response import Response

from .models import Style, Item, Tag, Review


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerialzier(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    "Создание комментария"

    class Meta:
        model = Review
        exclude = ('author', )


class ReviewRetrieveSerializer(serializers.ModelSerializer):
    """Вывод комментария"""
    children = RecursiveSerialzier(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = '__all__'


class StyleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.CharField(read_only=True)
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, slug_field='title')
    reviews = ReviewRetrieveSerializer(many=True)

    class Meta:
        model = Style
        exclude = ('id',)
        # depth = 1


class StyleSerializerUser(serializers.ModelSerializer):
    # items = ItemSerializerUser(many=True, read_only=True)
    items = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    categories = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    tags = serializers.SlugRelatedField(slug_field='title', many=True, queryset=Tag.objects.all())

    class Meta:
        model = Style
        fields = ('title', 'author', 'slug', 'items', 'categories', 'tags')


class ItemSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
