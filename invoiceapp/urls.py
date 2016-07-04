from django.conf.urls import url
from . import views

app_name = "invoiceapp"

urlpatterns = [

    url(r'^raiseinvoice/$', views.RaiseInvoice.as_view(),name='raiseinvoice'),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^account/$', views.Account.as_view(),name='account'),
    url(r'^estimates/$', views.Estimates,name='estimates'),
    url(r'^status/(?P<id>[0-9]+)/$' , views.Changestatus , name='changestatus'),

]
