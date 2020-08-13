from django.urls import path
from .views import *

app_name="Testapi"

urlpatterns=[
  path('api/insert_data',labdata,name='labdata'),
]