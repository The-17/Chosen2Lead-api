from django.contrib import admin
from .models import Company, Service, faq


admin.site.register(Company)
admin.site.register(Service)
admin.site.register(faq)
