from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', null=False, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name


