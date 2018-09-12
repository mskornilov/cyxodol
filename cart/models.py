from django.db import models

# Create your models here.
class Delivery_method(models.Model):
    method = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()

    def __str__(self):
        return '{}: стоимость доставки: {} руб.'.format(self.method, self.price)


class Order(models.Model):
    cart = models.TextField()
    delivery_method = models.ForeignKey(Delivery_method, null=True,
                                        on_delete=models.SET_NULL)
    name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    post_index = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    private_info_agreement = models.BooleanField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True,)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
