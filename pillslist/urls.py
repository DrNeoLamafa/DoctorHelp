from django.urls import path  
from django.contrib.auth import views as auth_views  



from .views import *  

app_name = 'pillslist'  
urlpatterns = [
    
    
    path('add/', pills_add, name='add'),
    path('', pills_detail, name='pills_detail'),
    path(r'^remove/(?P<product_id>)', pills_remove, name='pills_remove')
     
]