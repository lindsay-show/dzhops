from django.contrib import admin
from hostlist.models import HostList, CmccUser, DataCenter, Catagory
# Register your models here.

admin.site.register(HostList)
admin.site.register(CmccUser)
admin.site.register(DataCenter)
admin.site.register(Catagory)