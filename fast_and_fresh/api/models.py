from django.db import models

# Create your models here.


class Product (models.Model):
    product_name = models.CharField(max_length=30, null=True)
    is_special = models.BooleanField()

    def __str__(self):
        return self.product_name


class Batch (models.Model):
    product_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE, null=False, blank=False)
    units = models.IntegerField()
    elaboration_date = models.DateField()
    expiration_date = models.DateField()
    price_dolars_u = models.FloatField()
    units_sold = models.IntegerField(default=0)
    units_lost = models.IntegerField(default=0)


class Type_Of_Product (models.Model):
    type = models.CharField(max_length=50, editable=False)

    def __str__(self):
        return self.type


class Product_Type (models.Model):
    product_id = models.ForeignKey(
        'Product', on_delete=models.CASCADE, null=False, blank=False)
    type_of_product_id = models.ForeignKey(
        'Type_Of_Product', on_delete=models.CASCADE, null=False, blank=False)


class Client (models.Model):
    GENDER = ('F', ('Femenine')), ('M', ('Masculine'))
    client_name = models.CharField(max_length=100)
    client_last_name = models.CharField(max_length=100)
    client_cedula = models.IntegerField(null=True)
    client_phone = models.IntegerField(null=True)
    client_gender = models.CharField(
        max_length=1, choices=GENDER, blank=False, null=False)
    client_birthday = models.DateField()

    def __str__(self):
        return self.client_name


class Member (models.Model):

    member_points = models.IntegerField(default=0)
    member_email = models.EmailField()
    member_start_date = models.DateField(auto_now_add=True)
    member_end_date = models.DateField()
    zona = models.ForeignKey(
        'Zona', on_delete=models.CASCADE, null=False, blank=False)
    client = models.OneToOneField(
        'Client', on_delete=models.CASCADE, null=False, blank=False)


class Zona (models.Model):
    zona_name = models.CharField(max_length=30)
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.zona_name


class City (models.Model):
    city_name = models.CharField(max_length=30)
    state = models.ForeignKey(
        'State', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.city_name


class State (models.Model):
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return self.state_name


class Store (models.Model):
    store_name = models.CharField(max_length=30, null=True)
    zona = models.ForeignKey(
        'Zona', on_delete=models.CASCADE, null=False, blank=False)
    open_time = models.TimeField()
    closing_time = models.TimeField()
    store_phone = models.IntegerField(unique=True)
    supervisor=models.OneToOneField(
        'Employee', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.store_name


class Delivery (models.Model):
    STATUS = ('Entregado', ('Entregado')), ('No Entregado', ('No Entregado'))
    delivery_price = models.FloatField()
    delivery_transport=models.ForeignKey(
        'Transport', on_delete=models.CASCADE, null=False, blank=False)
    empleado=models.ForeignKey(
        'Employee', on_delete=models.CASCADE, null=False, blank=False)
    bill_id=models.ForeignKey(
        'Bill', on_delete=models.CASCADE, null=False, blank=False)
    delivery_status = models.CharField(
        max_length=15, choices=STATUS, blank=False, null=False)
    zona = models.ForeignKey(
        'Zona', on_delete=models.CASCADE, null=False, blank=False)
    address = models.CharField(max_length=200)


class PickUp (models.Model):
    STATUS = ('Entregado', ('Entregado')), ('No Entregado', ('No Entregado'))
    pickup_status = models.CharField(
        max_length=15, choices=STATUS, blank=False, null=False)
    bill_id=models.ForeignKey(
        'Bill', on_delete=models.CASCADE, null=False, blank=False)


class Transport (models.Model):
    BRAND = ('TOYOTA', ('TOYOTA')), ('FORD', ('FORD')), ('HONDA', ('HONDA'))
    transport_plate = models.CharField(max_length=7)
    transport_model = models.CharField(max_length=30)
    transport_brand = models.CharField(max_length=10, choices=BRAND)


class Bill (models.Model):
    cash_register_id =models.ForeignKey(
        'CashRegister', on_delete=models.CASCADE, null=False, blank=False)
    client_id = models.ForeignKey( 
        'Client', on_delete=models.CASCADE, null=False, blank=False)
    bill_sub_total = models.FloatField()
    bill_iva = models.ForeignKey(
        'IVA', on_delete=models.CASCADE, null=False, blank=False)
    bill_date = models.DateField(auto_now_add=True)
    bill_time = models.TimeField(auto_now_add=True)
    bill_sale = models.FloatField()
    bill_delivery = models.BooleanField()


class BillDetails (models.Model):
    bill_id = models.ForeignKey(
        'Bill', on_delete=models.CASCADE, null=False, blank=False)
    product_batch = models.ForeignKey(
        'Batch', on_delete=models.CASCADE, null=False, blank=False)
    product_quantity = models.IntegerField()


class CashRegister (models.Model):
    store_id = models.ForeignKey(
        'Store', on_delete=models.CASCADE, null=False, blank=False)


class PaymentMethod (models.Model):
    payment_method = models.CharField(max_length=20)


class Currency (models.Model):
    currency_name = models.CharField(max_length=20)


class CashRegisterIncome(models.Model):
    cash_register_id = models.ForeignKey(
        'CashRegister', on_delete=models.CASCADE, null=False, blank=False)
    day_income_total = models.FloatField()
    income_date = models.DateField(auto_now_add=True)


class ExchangeRate (models.Model):
    origin_currency = models.ForeignKey(
        'Currency', on_delete=models.CASCADE, null=False, blank=False)
    # destination_currency = models.ForeignKey(
    #     'Currency', on_delete=models.CASCADE, null=False, blank=False)
    exchange_rate = models.FloatField()

class Employee (models.Model):
    GENDER = ('F', ('Femenine')), ('M', ('Masculine'))
    employee_name=models.CharField(max_length=30)
    employee_last_name=models.CharField(max_length=30)
    employee_cedula=models.IntegerField(unique=True)
    employee_gender= models.CharField(
        max_length=1, choices=GENDER, blank=False, null=False)
    employee_birth_date=models.DateField()
    employee_phone=models.IntegerField()
    employee_store = models.ForeignKey(
        'Store', on_delete=models.CASCADE, null=False, blank=False)
    employee_job = models.ForeignKey(
        'Job', on_delete=models.CASCADE, null=False, blank=False)

class Job(models.Model):
    job_name=models.CharField(max_length=30)
    job_salary=models.FloatField

class IVA(models.Model):
    iva_porcentaje=models.FloatField
    iva_date=models.DateField(auto_now_add=True)
