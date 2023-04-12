from django.urls import path
from django.conf.urls import url
from . import views
from.views import *

urlpatterns = [

     path('', views.index, name='index'),
     path('bio', views.bio, name='bio'),
     path('contacts', views.contacts, name='contacts'),
     path('galleries',views.galleries, name='galleries'),
     path('gallery/<int:gallery_pk>/',get_gallery),




]