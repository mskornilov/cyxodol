from django.urls import path
from . import views
app_name = 'store'

urlpatterns = [
    path('<int:category_id>/<int:product_id>', views.product_details, name='product_details'),
    path('<int:category_id>/', views.products, name='products_by_cat'),
    path('', views.products, name='products'),
]
