from django.contrib import admin
from .models import Coupon, Category, UserProfile

models = [Coupon, Category, UserProfile]
for model in models:
    admin.site.register(model)
