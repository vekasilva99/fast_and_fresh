from api.models import Product
from api.models import Batch
from api.models import Type_Of_Product
from api.models import Product_Type
from api.models import Client
from api.models import Member
from api.models import Zone
from api.models import City
from api.models import State
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer
from .serializers import BatchSerializer
from .serializers import Type_Of_ProductSerializer
from .serializers import Product_TypeSerializer
from .serializers import ClientSerializer
from .serializers import MemberSerializer
from .serializers import ZoneSerializer
from .serializers import CitySerializer
from .serializers import StateSerializer


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


# Batch ViewSet
class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BatchSerializer


# Type_Of_Product ViewSet
class Type_Of_ProductViewSet(viewsets.ModelViewSet):
    queryset = Type_Of_Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Type_Of_ProductSerializer


# Product_Type ViewSet
class Product_TypeViewSet(viewsets.ModelViewSet):
    queryset = Product_Type.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Product_TypeSerializer


# Client ViewSet
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer


# Member ViewSet
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MemberSerializer


# Zone ViewSet
class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ZoneSerializer


# City ViewSet
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer


# State ViewSet
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StateSerializer
