 
from books import views
from django.urls import re_path , include

urlpatterns = [
    re_path('^$', views.index2, name='index'),
    
]