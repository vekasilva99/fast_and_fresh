from rest_framework import routers
from .api2 import ProductViewSet
from .api2 import BatchViewSet
from .api2 import Type_Of_ProductViewSet
from .api2 import Product_TypeViewSet
from .api2 import ClientViewSet
from .api2 import MemberViewSet
from .api2 import ZoneViewSet
from .api2 import CityViewSet
from .api2 import StateViewSet

router = routers.DefaultRouter()
router.register('api2/tables', ProductViewSet, 'tables')
# Completar con demás tablas
# Solo esta la de Productos --- prueba
urlpatterns = router.urls
