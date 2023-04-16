from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Client
from django.contrib.auth.hashers import make_password
admin.site.unregister(Group)


admin.site.site_header='Auto Services'
admin.site.site_title='Auto Services'
admin.site.site_url='http://127.0.0.1:8000/home/'


class ClientAdmin(admin.ModelAdmin):
     list_display = ("username","is_superuser","is_staff")
     def save_model(self, request, obj, form, change):
        obj.password = make_password(request.POST['password'])
        obj.save()

admin.site.register(Client,ClientAdmin)