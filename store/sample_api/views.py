from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from office.models import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@csrf_exempt
@api_view(['POST'])
def Createemployee(request):

    request_json = request.data

    o = offices.objects.get(officecode=1)
    request_json.update({"officecode":o})

    try:
        e = employees.objects.create(**request_json)
        msg = 'employee created'
    except Exception as e:
        msg = str(e)

    return Response({'message':msg},status=status.HTTP_200_OK)



