from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import JobApplication

class JobApplicationCreateView(CreateView):
    model = JobApplication
    fields = ["job_seeker", "job", "status"]
    template_name = "applications/create_job_application.html"

    def form_valid(self, form):
        form.instance.job_seeker = self.request.user.jobseeker
        return super().form_valid(form)
    
    def get_success_url(self):
        return redirect('job_list')