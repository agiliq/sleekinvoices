# Third Party Stuff
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group




class MyAdminSite(AdminSite):
    site_header = 'Sleekinvoice administration'
    site_title = 'Sleekinvoice site admin'
    index_title = 'Sleekinvoice site administration'

admin_site = MyAdminSite(name='Sleekinvoice')

admin_site.register(Group)
