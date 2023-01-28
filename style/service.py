from django_filters import rest_framework as filters
from style.models import Style, Tag


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class StyleFilter(filters.FilterSet):
    total_price = filters.RangeFilter()
    category = CharFilterInFilter(field_name='categories__title', lookup_expr='in')
    gender = filters.ChoiceFilter(choices=Style.GENDER_CHOICES)
    tags = filters.ModelMultipleChoiceFilter(field_name='tags__title', to_field_name='title',
                                             queryset=Tag.objects.all())

    class Meta:
        model = Style
        fields = ['total_price', 'category', 'gender']
