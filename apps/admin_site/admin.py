from django.contrib.admin import AdminSite
from django.http import HttpResponse

from . import views


class ThrillAdmin(AdminSite):

     def get_urls(self):
         from django.conf.urls import url
         urls = super(ThrillAdmin, self).get_urls()
         urls += [
             url(r'^online-users/$', self.admin_view(views.online_users))
         ]
         return urls


admin_site = ThrillAdmin()