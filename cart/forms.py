from django import forms
from .models import Order, Delivery_method

class OrderForm(forms.ModelForm):
    # delivery_field = forms.ModelChoiceField(queryset=Delivery_method.objects.all(),
    #                                         to_field_name='method')
    class Meta:
        model = Order
        fields = ['delivery_method', 'name', 'email', 'phone_number',
                'address', 'post_index', 'region', 'private_info_agreement',
                'comment']


class Delivery_methodForm(forms.ModelForm):
    class Meta:
        model = Delivery_method
        fields = ['method', 'price']
