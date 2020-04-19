from django.urls import path
from . import views


urlpatterns=[ 
    path('home',views.index,name='home'),
    path('addProduct',views.addProduct,name='addProduct'),
    path('addProject',views.addProject,name='addProject'),
    path('displayProject',views.displayProject,name='displayProject'),
    path('addSupplier',views.addSupplier,name='addSupplier'),
    path('payment',views.payment,name='payment'),
    path('approve',views.approve,name='approve'),
    path('viewAll',views.viewAll,name='viewAll')
    ]

