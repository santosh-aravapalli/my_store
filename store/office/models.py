from django.db import models

# Create your models here.


class productline(models.Model):
    productline = models.CharField(max_length=50,primary_key=True)
    textdescription = models.TextField(max_length=4000)

    def __str__(self):
        return self.productline

class product(models.Model):
    productcode = models.CharField(max_length=15,primary_key=True)
    productname = models.CharField(max_length=70)
    productline = models.ForeignKey(productline,on_delete=models.CASCADE)
    productscale = models.CharField(max_length=10)
    productvendor = models.CharField(max_length=50)
    productdescription = models.TextField(max_length=5000)
    quantity_instock = models.SmallIntegerField()
    buyprice = models.DecimalField(max_digits=10,decimal_places=2)
    msrp = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.productcode

class offices(models.Model):
    officecode = models.CharField(max_length=10,primary_key=True)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(max_length=50)
    addressline2 = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=15)
    territory = models.CharField(max_length=10)

    def __str__(self):
        return self.officecode

class employees(models.Model):
    employeenumber = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    extension = models.CharField(max_length=10)
    email = models.EmailField()
    officecode = models.ForeignKey(offices,on_delete=models.CASCADE)
    reports_to = models.ForeignKey('employees',models.SET_NULL,null=True,blank=True)
    jobtitle = models.CharField(max_length=50)
    salary = models.BigIntegerField(default=100000)


    def __str__(self):
        return '%s : %s'%(self.employeenumber,self.firstname)

class customers(models.Model):
    custmorenumber = models.IntegerField(primary_key=True)
    customername = models.CharField(max_length=50)
    contact_lastname = models.CharField(max_length=50)
    contact_firstname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(max_length=50)
    addressline2 = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50,null=True)
    postalcode = models.CharField(max_length=15,null=True)
    country = models.CharField(max_length=50)
    sales_rep_no = models.ForeignKey(employees,models.SET_NULL,null=True)
    credit_limit = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return "%s : %s"%(self.custmorenumber,self.customername)

class orders(models.Model):
    ordernumber = models.IntegerField(primary_key=True)
    order_date = models.DateField()
    required_date = models.DateField()
    shippeddate = models.DateField(null=True)
    status = models.CharField(max_length=15)
    comments = models.TextField(max_length=8000,null=True)
    custmomer_no = models.ForeignKey(customers,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ordernumber)

class orderdetails(models.Model):
    ordernumber = models.ForeignKey(orders,on_delete=models.CASCADE)
    productcode = models.ForeignKey(product,on_delete=models.CASCADE)
    quantityordered = models.IntegerField()
    price_each = models.DecimalField(max_digits=10,decimal_places=2)
    orderedlinenumber = models.SmallIntegerField()

    def __str__(self):
        return str(self.ordernumber)

class payments(models.Model):
    customernumber = models.ForeignKey(customers,on_delete=models.CASCADE)
    checknumber = models.CharField(max_length=58,primary_key=True)
    paymentdate = models.DateField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.checknumber)



