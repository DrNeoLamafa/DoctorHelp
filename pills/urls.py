from django.urls import include, path
from .views  import *
app_name = 'pills_app'
urlpatterns = [
    path('', index, name='index'),
    path('search/', search),
    path('result/', result),
     
]