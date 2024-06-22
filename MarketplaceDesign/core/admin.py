from django.contrib import admin
from .models import Good, Cart, CartItem

# Register your models here.
admin.site.register(Good)
admin.site.register(Cart)
admin.site.register(CartItem)
