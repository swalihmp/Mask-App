from django.contrib import admin
from .models import users,mask,admins,order

# Register your models here.
admin.site.register(users)
admin.site.register(mask)
admin.site.register(admins)
admin.site.register(order)