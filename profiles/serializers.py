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

