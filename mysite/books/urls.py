#from django.conf.urls import url 
from . import views
from django.urls import re_path , include

urlpatterns = [
    re_path('^$', views.index, name='index'),
    
    
]