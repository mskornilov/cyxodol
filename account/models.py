from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

User.add_to_class('cart', models.TextField(default=[]))
