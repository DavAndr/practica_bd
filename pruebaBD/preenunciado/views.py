from rest_framework import viewsets
from preenunciado.models import *
from preenunciado.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import renderers, status

from django.db.models import F, Sum
# Create your views here.

class CategoriesViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    #@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    #def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)



class CustomercustomerdemoViewset(viewsets.ModelViewSet):
    queryset = Customercustomerdemo.objects.all()
    serializer_class = CustomercustomerdemoSerializer

class CustomerdemographicsViewset(viewsets.ModelViewSet):
    queryset = Customerdemographics.objects.all()
    serializer_class = CustomerdemographicsSerializer

class CustomersViewset(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class EmployeeterritoriesViewset(viewsets.ModelViewSet):
    queryset = Employeeterritories.objects.all()
    serializer_class = EmployeeterritoriesSerializer

class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class OrderdetailsViewset(viewsets.ModelViewSet):
    queryset = Orderdetails.objects.all()
    serializer_class = OrderdetailsSerializer

class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def create(self,request,*args, **kwargs):
        serializer = self.get_serializer(data = request.data)

        

        if serializer.is_valid():
            r= {}

            customerid = serializer.data.get("customerid")
            employeeid = serializer.data.get("employeeid")
            shipvia = serializer.data.get("shipvia")
            supplierID = serializer.data.get("supplierID")
            categoryID = serializer.data.get("categoryID")
            stockRequerido = serializer.data.get("stockRequerido")
            
            productos = Products.objects.all().annotate(stock_futuro = F('unitsinstock') + F('unitsonorder')).filter(stock_futuro__lt = stockRequerido)
            supplier = Suppliers.objects.get(supplierid = supplierID)
            #productoSerializer = ProductsSerializer(productos,many=True)

            o = Orders(customerid= Customers.objects.get(customerid= customerid), employeeid= Employees.objects.get(employeeid=employeeid) , orderdate= "1111-11-11",requireddate= "1111-11-11",shippeddate= "1111-11-11",shipvia=Shippers.objects.get(shipperid =shipvia),freight= 0,shipname=supplier.companyname,shipaddress=supplier.address,shipcity=supplier.city,shipregion=supplier.region,shippostalcode=supplier.postalcode,shipcountry=supplier.country)
            o_serialized = Full_OrdersSerializer(o)
            r.update(o_serialized.data)
            
            nro= 0
            for y in productos:
                nro= nro+1
                q = stockRequerido - (y.unitsinstock + y.unitsonorder)
                descuento = 0.10

                if q < 100:
                    descuento= 0
                or_det =Orderdetails(orderid = o, productid= y, unitprice= y.unitprice,quantity = q,discount= descuento)
                print(or_det)

                or_det_serialized = OrderdetailsSerializer(or_det)
                r.update({"Order detail "+nro.__str__() : or_det_serialized.data})
            #return Response(productoSerializer.data)
            #serializer.save()
            return Response(r)
            
        return Response(serializer.errors)


class ProductsViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def list(self, request):
        suplierid = request.query_params.get('suplierid')
        categoryid = request.query_params.get('categoryid')
        stockmin = request.query_params.get('stockmin')

        queryset = Products.objects.all()
        stat= 200
        
        
        if suplierid:
            queryset = queryset.filter(supplierid = suplierid)

        if categoryid:
            queryset = queryset.filter(categoryid = categoryid)
        
        if stockmin:
            queryset = queryset.filter(unitsinstock__gte = stockmin)

        if suplierid or categoryid:
            if stockmin:
                stat=404
            else:
                stat=204
            queryset = queryset.exclude(discontinued="b'\\x00'")
            serializer= self.get_serializer(queryset,many = True)
            if serializer.data == []:
                return Response(status=stat)
        serializer = self.get_serializer(queryset,many = True)
        
        return Response(serializer.data, status= stat)

class RegionViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ShippersViewset(viewsets.ModelViewSet):
    queryset = Shippers.objects.all()
    serializer_class = ShippersSerializer

class SuppliersViewset(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

class TerritoriesViewset(viewsets.ModelViewSet):
    queryset = Territories.objects.all()
    serializer_class = TerritoriesSerializer
