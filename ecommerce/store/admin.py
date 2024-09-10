from django.contrib import admin

# Register your models here.


from django.contrib import admin

from .models import Cart, Products, Customer, Category

# Register your models here.
admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Category)
