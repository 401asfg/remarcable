from django.shortcuts import render
from django.db import connection, reset_queries

from django_tables2 import RequestConfig

from . import models
from . import filters
from . import tables


def product_list(request):
    qs = (
        models.Product.objects.all()
        .select_related('category')
        .prefetch_related('tags')
    )

    product_filter = filters.ProductFilter(request.GET, queryset=qs)

    if product_filter.is_valid():
        qs = product_filter.qs

    product_table = tables.ProductTable(qs)

    RequestConfig(request, paginate={"per_page": 10}).configure(product_table)

    context = {
        "product_filter": product_filter,
        "product_table": product_table,
    }

    return render(request, 'product_list.html', context)
