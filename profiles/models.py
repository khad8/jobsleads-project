from django.db import models
from django.contrib.auth.models import User

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="cvs/")
    skills = models.TextField(blank=True)
    experience = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.company