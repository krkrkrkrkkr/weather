from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("delete/<str:name>",views.delete,name='delete')
]