from django.conf.urls import url
from . import views

app_name = "invoiceapp"

urlpatterns = [

    url(r'^raiseinvoice/$', views.RaiseInvoice.as_view(),name='raiseinvoice'),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^account/$', views.Account.as_view(),name='account'),
	
	url(r'^update_account/(?P<pk>[0-9]+)/$' , views.AccountUpdate.as_view(),name='updateaccount'),
    url(r'^estimates/$', views.Estimates,name='estimates'),
	 url(r'^deleteclient/(?P<pk>[0-9]+)/$' , views.deleteclient , name='deleteclient'),# /*Functioning completed*/ 
    url(r'^status/(?P<id>[0-9]+)/$' , views.Changestatus , name='changestatus'),
    url(r'^login/$', views.login_user, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),
    url(r'^clients/$', views.client, name='client'),
    url(r'^add_client/$', views.add_client.as_view(),name='add_client'),
    url(r'^myinvoices/$', views.invoices_for_me, name='invoices_for_me'),
]
