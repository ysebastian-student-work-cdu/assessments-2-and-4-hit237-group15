from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Audit_Record)
admin.site.register(Food_Items)