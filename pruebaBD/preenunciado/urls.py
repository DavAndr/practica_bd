from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework import renderers
from .views import *

# categoria_list = CategoriesViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# categoria_detail = CategoriesViewset.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

router = routers.DefaultRouter()
router.register(r"Categories",views.CategoriesViewset,basename="Categories")
router.register(r"Customercustomerdemo",views.CustomercustomerdemoViewset,basename="Customercustomerdemo")
router.register(r"Customerdemographics",views.CustomerdemographicsViewset,basename="Customerdemographics")
router.register(r"Customers",views.CustomersViewset,basename="Customers")
router.register(r"Employeeterritories",views.EmployeeterritoriesViewset,basename="Employeeterritories")
router.register(r"Employees",views.EmployeesViewset,basename="Employees")
router.register(r"Orderdetails",views.OrderdetailsViewset,basename="Orderdetails")
router.register(r"Orders",views.OrdersViewset,basename="Orders")
router.register(r"Products",views.ProductsViewset,basename="Products")
router.register(r"Region",views.RegionViewset,basename="Region")
router.register(r"Shippers",views.ShippersViewset,basename="Shippers")
router.register(r"Suppliers",views.SuppliersViewset,basename="Suppliers")
router.register(r"Territories",views.TerritoriesViewset,basename="Territories")


urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('snippets/', categoria_list, name='categoria-list'),
#     path('snippets/<int:pk>/', categoria_detail, name='id'),
# ]