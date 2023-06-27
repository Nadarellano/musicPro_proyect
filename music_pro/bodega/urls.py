from django.urls import path, include
from .views import *
from rest_framework import routers
from .serializers import *

router = routers.DefaultRouter()

router.register('bodega', BodegaViewset)



urlpatterns = [

    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
]