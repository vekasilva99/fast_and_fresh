from django.contrib import admin
from .models import Product, Client, Member,Zona,City,State, Product_Type, Type_Of_Product, Batch

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'product_name', 'is_special')

class Type_of_Product_Admin(admin.ModelAdmin):
    list_display=('id', 'type')

class Product_Type_Admin(admin.ModelAdmin):
    list_display=('product_id', 'type_of_product_id')

class BatchAdmin(admin.ModelAdmin):
    list_display=('product_id', 'units', 'elaboration_date', 'expiration_date', 'price_dolars_u','units_sold', 'units_lost')

class ClientAdmin(admin.ModelAdmin):
    list_display=('id', 'client_name', 'client_last_name', 'client_cedula')

class MemberAdmin(admin.ModelAdmin):
    list_display=('id', 'member_email', 'member_points', 'client')

class ZonaAdmin(admin.ModelAdmin):
    list_display=('id', 'zona_name', 'city')

class CityAdmin(admin.ModelAdmin):
    list_display=('id', 'city_name', 'state')

class StateAdmin(admin.ModelAdmin):
    list_display=('id', 'state_name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Product_Type, Product_Type_Admin)
admin.site.register(Type_Of_Product, Type_of_Product_Admin)
admin.site.register(Batch, BatchAdmin)


