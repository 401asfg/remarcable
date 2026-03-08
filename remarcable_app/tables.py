import django_tables2 as tables
from . import models


class ProductTable(tables.Table):
    name = tables.Column(verbose_name="Name")
    category = tables.Column(verbose_name="Category", accessor='category.name')
    tags = tables.Column(verbose_name="Tags", accessor='tags.all')
    description = tables.Column(verbose_name="Description")

    class Meta:
        model = models.Product
        fields=['name', 'category', 'tags', 'description']
        order_by=('category', 'name')
        empty_text = "No products found"
    
    def render_tags(self, value):
        tag_names = value.values_list('name', flat=True)
        return ", ".join(tag_names)
