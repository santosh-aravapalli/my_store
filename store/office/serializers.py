from .models import *
from rest_framework.serializers import ModelSerializer


class productserializer(ModelSerializer):

    class Meta:
        model = product
        fields = "__all__"


class employeeserializer(ModelSerializer):

    class Meta:
        model = employees
        fields = "__all__"


class customerserializer(ModelSerializer):

    class Meta:
        model = customers
        fields = "__all__"

