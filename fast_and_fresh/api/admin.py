from django.contrib import admin
from .models import Product, Client, Member, Zona, City, State, Product_Type, Type_Of_Product, Batch, Store, Delivery, PickUp, Bill, BillDetails, Currency, ExchangeRate, CashRegister, CashRegisterIncome, PaymentMethod, Employee, Job, IVA

# Register your models here.


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_price', 'delivery_transport',
                    'empleado', 'bill_id', 'delivery_status', 'zona', 'address')


class PickUpAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_status', 'bill_id')


class TransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'transport_plate',
                    'transport_model', 'transport_brand')


class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'cash_register_id', 'client_id', 'bill_sub_total',
                    'bill_iva', 'bill_date', 'bill_time', 'bill_sale', 'bill_delivery')


class BillDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill_id', 'product_batch',
                    'product_batch', 'product_quantity')


class CashRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'store_id')



class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_method')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_name')


class CashRegisterIncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cash_register_id', 'day_income_total', 'income_date')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id', 'employee_name', 'employee_last_name', 'employee_cedula', 'employee_gender', 'employee_birth_date', 'employee_phone', 'employee_store', 'employee_job')

class JobAdmin(admin.ModelAdmin):
    list_display=('id', 'job_name', 'job_salary')

class IVAAdmin(admin.ModelAdmin):
    list_display=('id','iva_porcentaje', 'iva_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'is_special')


class Type_of_Product_Admin(admin.ModelAdmin):
    list_display = ('id', 'type')


class Product_Type_Admin(admin.ModelAdmin):
    list_display = ('product_id', 'type_of_product_id')


class BatchAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'units', 'elaboration_date',
                    'expiration_date', 'price_dolars_u', 'units_sold', 'units_lost')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_last_name', 'client_cedula')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_email', 'member_points', 'client')


class ZonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'zona_name', 'city')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'state')


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_name')


class StoreAdmin (admin.ModelAdmin):
    list_display = ('id', 'store_name', 'open_time',
                    'closing_time', 'store_phone', 'supervisor')


# Registrar los modelos

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Product_Type, Product_Type_Admin)
admin.site.register(Type_Of_Product, Type_of_Product_Admin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(PickUp, PickUpAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(BillDetails, BillDetailsAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangeRate)
admin.site.register(CashRegister, CashRegisterAdmin)
admin.site.register(CashRegisterIncome, CashRegisterIncomeAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(IVA, IVAAdmin)
