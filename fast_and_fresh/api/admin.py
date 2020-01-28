from django.contrib import admin
from .models import Product, Client, Member,Zona,City,State

# Register your models here.

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Member)
admin.site.register(Zona)
admin.site.register(City)
admin.site.register(State)

