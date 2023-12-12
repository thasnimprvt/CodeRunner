from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path("extract/<pk>",views.extract,name='extract'),
    path("delete/<pk>",views.delete, name='delete'),
    path("extract/",views.extracting,name='extracting'),
    # path("extract/",views.out,name='output'),

]