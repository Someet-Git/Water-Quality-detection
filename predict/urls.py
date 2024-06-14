from django.urls import path,include

from . import views

urlpatterns=[
    path("",views.index, name='index'),
    path("index",views.index, name='index'),
    path("about", views.about, name='about')
    ]
