from rest_framework import serializers

from .models import Style, User, Item


class ItemSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'slug', 'image', 'price')


class StyleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.CharField(read_only=True)
    # categories = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    # tags = serializers.SlugRelatedField(read_only=True, many=True, slug_field='title')
    items = ItemSerializerUser(read_only=True, many=True)

    class Meta:
        depth = 1
        model = Style
        exclude = ('id',)


class StyleSerializerUser(serializers.ModelSerializer):
    items = ItemSerializerUser(many=True, read_only=True)
    categories = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)
    tags = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)

    class Meta:
        model = Style
        fields = ('title', 'author', 'slug', 'items', 'categories', 'tags')


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    subscribers = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    subscriptions = serializers.SlugRelatedField(slug_field='username', queryset=User.objects, many=True)
    styles = StyleSerializerUser(many=True, read_only=True)
    # instagram = serializers.Fiel

    class Meta:
        model = User
        fields = (
            'username',
            'instagram',
            'telegram',
            'whatsapp',
            'description',
            'subscriptions',
            'subscribers',
            'date_joined',
            'image',
            'styles',
            'favorites',
        )


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'pk')


class ItemSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Item
        fields = '__all__'
