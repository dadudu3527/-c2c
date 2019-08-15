from django.contrib import admin
from buyer_apps.user.models import User,Address


# Register your models here.
admin.site.register(User)
admin.site.register(Address)