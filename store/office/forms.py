from django.forms import ModelForm
from .models import *


class employeeform(ModelForm):

    class Meta:
        model = employees
        fields = "__all__"


class customersform(ModelForm):

    class Meta:
        model = customers
        fields = "__all__"


class orderform(ModelForm):

    class Meta:
        model = orders
        fields = "__all__"


class officeform(ModelForm):
    
    class Meta:
        model = offices
        fields = "__all__"
        
