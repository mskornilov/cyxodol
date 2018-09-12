from django.contrib import admin
from .models import Delivery_method, Order
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'delivery_method', 'name', 'email',
                    'phone_number', 'address', 'post_index', 'region',
                    'private_info_agreement', 'created', 'completed']
    list_filter = ['created']

admin.site.register(Delivery_method)
