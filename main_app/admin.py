from django.contrib import admin

# Register your models here.
from django.contrib import admin
# import your models here
from .models import JobListing, Employer, StaffRegister

# Register your models here
admin.site.register(JobListing)
admin.site.register(Employer)
admin.site.register(StaffRegister)
