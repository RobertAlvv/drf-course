from django.contrib import admin
from apps.products.models import Product, CategoryProduct, MeasureUnit, Indicator

admin.site.register(MeasureUnit)
admin.site.register(CategoryProduct)
admin.site.register(Product)
admin.site.register(Indicator)
