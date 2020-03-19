from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product Admin Definition """
    list_display = ("title", "low_price", "n_review", "category")