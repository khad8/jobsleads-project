from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Job


class JobListView(ListView):
    model = Job
    template_name = "job_list.html"
    context_object_name = "jobs"
    queryset = Job.objects.all()


class JobDetailView(DetailView):
    model = Job
    template_name = "job_detail.html"
    

class JobCreateView(CreateView):
    model = Job
    template_name = "job_create.html"
    fields = ["title", "recruiter", "salary", "location", "category" ,"job_types"]
    success_url = reverse_lazy('job_list')


    def form_valid(self, form):
        return super().form_valid(form)
    

class JobUpdateView(UpdateView):
    model = Job
    template_name = "job_create.html"
    fields = ["title", "recruiter", "salary", "location", "category" ,"job_types"]
    success_url = reverse_lazy('job_list')

    def form_valid(self, form):
        return super().form_valid(form)



class JobDeleteView(DeleteView):
    model = Job
    template_name = "job_delete.html"
    success_url = reverse_lazy('job_list')