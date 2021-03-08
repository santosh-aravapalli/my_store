"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from office.views import employeeregister, home, productview, orderview, orderdetailview, employeeapiview, officecodeapi
from rest_framework.routers import DefaultRouter

emp_router = DefaultRouter()
emp_router.register('employee',employeeapiview)




urlpatterns = [

    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("product/",productview,name="products"),
    path("employees/",employeeregister,name="employees"),
    path("orders/",orderview,name="order"),
    path("orderdetail/<str:order_number>/",orderdetailview,name="orderdetail"),
    path("api/",include(emp_router.urls)),
    path("office/<str:off_code>",officecodeapi,name="off_code_api"),

]

