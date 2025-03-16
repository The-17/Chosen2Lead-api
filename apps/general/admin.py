from django.contrib import admin
from .models import Company, Service, faq, Inquiry, JobApplication


admin.site.register(Company)
admin.site.register(Service)
admin.site.register(faq)
admin.site.register(Inquiry)
admin.site.register(JobApplication)
