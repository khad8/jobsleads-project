from django.db import models


class JobCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    recruiter = models.ForeignKey(
        'profiles.Recruiter',
        on_delete=models.CASCADE
    )

    location = models.CharField(max_length=200)
    job_types = models.CharField(
        max_length=50,
        choices=[('Full-time', 'Full time'), ('Part-time', 'Part time')]
    )
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)

    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title