from django.contrib import admin

# Register your models here.

from .models import Event, Organization, EventVol, OrganizationUsers, Job

admin.site.register(Event)
admin.site.register(Organization)
admin.site.register(EventVol)
admin.site.register(OrganizationUsers)
admin.site.register(Job)
