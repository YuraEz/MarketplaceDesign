from django.db import models
from django.contrib.auth.models import User


class Good(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    img = models.ImageField(upload_to="good/%Y/%m/%d/", null=True, blank=True)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'

    def __str__(self):
        return f"Good's name: {self.name}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods_in_cart = models.ManyToManyField(to=Good)
    created_time = models.DateTimeField(auto_now_add=True)

    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    in_order = models.BooleanField(default=False)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def total_price(self):
        return self.good.price * self.quantity