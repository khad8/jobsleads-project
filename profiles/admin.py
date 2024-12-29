from django.contrib import admin

from .models import JobSeeker, Recruiter

admin.site.register(JobSeeker)
admin.site.register(Recruiter)