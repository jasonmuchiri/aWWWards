from django.conf.urls import url
from . import views

urlpattern=[
    url('^$',views.index,name = 'index'),
]