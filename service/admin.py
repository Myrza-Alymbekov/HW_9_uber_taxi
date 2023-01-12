from django.contrib import admin

from .models import StatusType, StatusDriver

admin.site.register(StatusType)
admin.site.register(StatusDriver)
