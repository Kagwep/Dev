import imp
from django.urls import path
from . import views

urlpatterns = [
    path('l',views.getData),
    path('add',views.addItem),
]
