# service_requests/admin.py

from django.contrib import admin
from .models import ServiceRequest, CustomerProfile, SupportRepresentative

# Register the models to make them available in the admin interface
admin.site.register(ServiceRequest)
admin.site.register(CustomerProfile)
admin.site.register(SupportRepresentative)
