from rest_framework import serializers

from .models import Style, Item


class ItemSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'slug', 'image', 'price')
        extra_kwargs = {
            'title': {'source': 'slug', 'read_only': True}
        }


class StyleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.CharField(read_only=True)
    items = ItemSerializerUser(read_only=True, many=True)
    categories = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    tags = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')

    class Meta:
        # depth = 1
        model = Style
        exclude = ('id',)


class StyleSerializerUser(serializers.ModelSerializer):
    items = ItemSerializerUser(many=True, read_only=True)
    categories = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    tags = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)

    class Meta:
        model = Style
        fields = ('title', 'author', 'slug', 'items', 'categories', 'tags')


class ItemSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
