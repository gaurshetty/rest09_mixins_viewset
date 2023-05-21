from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

routerviewset = SimpleRouter()
routerviewset.register('', EmployeeMixinViewSet, basename='Employeeviewset')

urlpatterns = [
    path('', include(routerviewset.urls)),
]
