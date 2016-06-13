from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name