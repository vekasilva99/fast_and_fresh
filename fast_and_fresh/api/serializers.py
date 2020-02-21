from rest_framework import serializers
from api.models import Product
from api.models import Batch
from api.models import Type_Of_Product
from api.models import Product_Type
from api.models import Client
from api.models import Member
from api.models import Zone
from api.models import City
from api.models import State

# Product Serializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Batch Serializer
class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


# Type_Of_Product Serializer
class Type_Of_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Of_Product
        fields = '__all__'


# Product_Type Serializer
class Product_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Type
        fields = '__all__'


# Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


# Member Serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


# Zone Serializer
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


# City Serializer
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


# State Serializer
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
