from django.urls import path
from .views import home, galeria

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
]