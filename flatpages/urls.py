from django.urls import path
from . import views

app_name = 'flatpages'

urlpatterns=[
    path('about-us/', views.about_us, name='about_us'),
    path('faq/', views.faq, name='faq'),
    path('contacts/', views.contacts, name='contacts'),
    path('opt/', views.opt, name='opt'),
    path('', views.index, name='index'),

]
