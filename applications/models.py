from django.db import models


class ApplicationStatus(models.Model):
    status = models.CharField(max_length=200)


class JobApplication(models.Model):
    job_seeker = models.ForeignKey(
        'profiles.JobSeeker',
        on_delete=models.CASCADE
        )
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Application by {self.job_seeker.user.username} for {self.job.title}"