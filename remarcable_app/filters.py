import django_filters as filters

from django.db.models import Q
from django import forms

from . import models


class SearchFilter(filters.CharFilter):
    """
    A filter that takes text as its input and retrieves all models instances that have 
    at least one field that contains the given search text
    """

    def __init__(self, fields: list[str], *args, **kwargs):
        """
        fields: The fields of the model to search for the given text in
        """
        self.fields = fields
        super().__init__(*args, **kwargs)

    def filter(self, queryset, value):
        if value is None or value == "":
            return queryset
        
        q = Q()
        for field in self.fields:
            q |= Q(**{f"{field}__icontains": value})
        
        return queryset.filter(q).distinct()


class ProductFilter(filters.FilterSet):
    q = SearchFilter(label="", fields=['name', 'description'])

    category = filters.ModelChoiceFilter(
        label="Category",
        queryset=models.Category.objects.all(),
        method="filter_category",
    )

    tags = filters.ModelMultipleChoiceFilter(
        field_name="tags",
        queryset=models.Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        method="filter_tags",
    )

    def filter_category(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(category=value)
    
    def filter_tags(self, queryset, name, values):
        if not values:
            return queryset

        q = Q()

        for value in values:
            q |= Q(tags=value)
        
        return queryset.filter(q).distinct()
    