from django.conf import settings
from django.urls import path, include
from .views import *
# from rest_framework.routers import DefaultRouter
# emp_router = DefaultRouter()
# emp_router.register('employee', employeeapiview)


urlpatterns = [

    path("createemployee/", Createemployee, name="products"),

]