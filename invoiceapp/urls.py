from django.conf.urls import url
from . import views

app_name = "invoiceapp"

urlpatterns = [

    url(r'^account/$', views.Account.as_view(),name='account'),
    url(r'^$', views.Index.as_view(), name='index'),

]

