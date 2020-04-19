from django.urls import path
from . import views
#from django.views.generic import TemplateView

urlpatterns=[
    #path('',TemplateView.as_view(template_name='bootstrap/loginLayout.html')),
    path('',views.loginPage,name='loginPage'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register')
    ]
