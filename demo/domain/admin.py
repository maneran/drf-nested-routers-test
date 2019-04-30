from django.contrib import admin

# Register your models here.
from .models import Domain, Nameserver

admin.site.register(Domain)
admin.site.register(Nameserver)