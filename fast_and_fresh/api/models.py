from django.db import models

# Create your models here.

class Product (models.Model):
    product_name = models.CharField(max_length=30,null=True)
    is_special = models.BooleanField()
    def __str__(self):
        return self.product_name

class Batch (models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False)
    units = models.IntegerField()
    elaboration_date= models.DateField()
    expiration_date = models.DateField()
    price_dolars_u = models.FloatField()
    units_sold = models.IntegerField()
    units_lost = models.IntegerField()


class Type_Of_Product (models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.type

class Product_Type (models.Model):
     product_id = models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False)
     type_of_product_id = models.ForeignKey('Type_Of_Product', on_delete=models.CASCADE, null=False, blank=False)
    

class Client (models.Model):
    GENDER=('F',('Femenine')), ('M',('Masculine'))
    client_name = models.CharField(max_length=100)
    client_last_name = models.CharField(max_length=100)
    client_cedula =  models.IntegerField(null=True)
    client_phone =  models.IntegerField(null=True)
    client_gender = models.CharField(max_length=30, choices=GENDER, blank=False, null=False)
    # client_birthday = models.DateField()



    def __str__(self):
        return self.client_name

class Member (models.Model):
    
    member_points = models.IntegerField(default=0)
    member_email = models.EmailField()
    member_start_date = models.DateField()
    member_end_date = models.DateField()
    zona = models.ForeignKey('Zona', on_delete=models.CASCADE, null=False, blank=False)
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





    



