from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.views.decorators.cache import cache_page

# Create your views here.


def home(request):
    return render(request,"home.html")


def employeeregister(request):

    return render(request,"home.html",{"employees":employees.objects.all()})


def productview(request):
    products=product.objects.all()
    return render(request,"home.html",{"product":products})


def orderview(request):
    order = orders.objects.all()
    return render(request,"order.html",{"orders":order})


def orderdetailview(request,order_number):
    order_detail = orderdetails.objects.filter(ordernumber=order_number)
    return render(request,"order_detail.html",{"orderdetail":order_detail})


class employeeapiview(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeeserializer

    def retrieve(self, request, pk=None):
        try:
            queryset = employees.objects.filter(officecode=pk)
            serializer = employeeserializer(data=queryset)
            return Response(serializer.data)
        except:
            queryset = employees.objects.all()
            serializer = employeeserializer(data=queryset)
            return Response(serializer.data)



@api_view(['GET',])
def officecodeapi(request,off_code):
    qs = employees.objects.filter(officecode=off_code)
    serializer = employeeserializer(qs,many=True)
    return Response(serializer.data)
