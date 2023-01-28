from rest_framework import serializers

from profiles.models import User
from style.serializers import StyleSerializerUser


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


class FollowersSerializer(serializers.Serializer):
    """Добавление в подписчики"""
    username = serializers.CharField(max_length=150)


# class ItemSerializerUser(serializers.ModelSerializer):
#     # items = serializers.SlugRelatedField(many=True, get_queryset=Style.objects.all())
#     #
#     class Meta:
#         model = Item
#
#         fields = ('title', 'slug', 'image', 'price')
#         extra_kwargs = {
#             'title': {'source': 'slug', 'read_only': True}
#         }

