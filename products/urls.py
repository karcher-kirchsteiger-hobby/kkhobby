from django.conf.urls import patterns, url

from products import views

urlpatterns = patterns('',
    url(r'list_products/$', views.list_products)
)

