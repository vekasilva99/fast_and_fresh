from django.db import models

# Create your models here.

class Product (models.Model):
    product_name = models.CharField(max_length=30,null=True)
    is_gluten_free = models.BooleanField()
    is_vegan = models.BooleanField()
    is_organic = models.BooleanField()
    is_special = models.BooleanField()
    product_price_dolar = models.FloatField(null=True)
    product_price_bolivares = models.FloatField(null=True)
    def __str__(self):
        return self.product_name

class Client (models.Model):
    client_name = models.CharField(max_length=100)
    client_last_name = models.CharField(max_length=100)
    client_cedula =  models.IntegerField(null=True)

    def __str__(self):
        return self.client_name

class Member (models.Model):
    GENDER=(('F',('Femenine')), ('M',('Masculine')))
    member_points = models.IntegerField(default=0)
    member_email = models.EmailField()
    member_birthday = models.DateField()
    member_start_date = models.DateField()
    member_end_date = models.DateField()
    member_gender = models.CharField(max_length=30, choices=GENDER)
    client = models.OneToOneField('Client',on_delete=models.CASCADE,null=False, blank=False)
    

    
class Zona (models.Model):
    zona_name = models.CharField(max_length=30)
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.zona_name

class City (models.Model):
    city_name = models.CharField(max_length=30)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.city_name

class State (models.Model):
    state_name = models.CharField(max_length=30)
    def __str__(self):
        return self.state_name





    



