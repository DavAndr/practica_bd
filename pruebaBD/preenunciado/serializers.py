from rest_framework import serializers
from preenunciado.models import *

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CustomercustomerdemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customercustomerdemo
        fields = '__all__'

class CustomerdemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customerdemographics
        fields = '__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class EmployeeterritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeeterritories
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class Full_OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):

    supplierID = serializers.PrimaryKeyRelatedField(required=False, queryset=Suppliers.objects.all())
    categoryID = serializers.PrimaryKeyRelatedField(required=False,queryset=Categories.objects.all())
    stockRequerido = serializers.IntegerField(required=False)
    class Meta:
        model = Orders
        fields = ['orderid','customerid','employeeid','shipvia','supplierID','categoryID','stockRequerido']

class ProductsSerializer(serializers.ModelSerializer):

    stockFuturo = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['productid','productname','unitprice','stockFuturo']
    
    def get_stockFuturo(self,obj):
        if obj.unitsinstock is not None and obj.unitsonorder is not None:
            return obj.unitsinstock + obj.unitsonorder
        return None

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ShippersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__'



class TerritoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territories
        fields = '__all__'


