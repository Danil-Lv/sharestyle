from rest_framework import serializers
from .models import Style
from .utils import make_slug


class StyleSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # slug = serializers.SlugField(default=make_slug())
    class Meta:
        model = Style
        exclude = ('id', )