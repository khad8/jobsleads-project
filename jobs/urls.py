from django.urls import path
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobDeleteView,
    JobUpdateView
)

urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("create/", JobCreateView.as_view(), name="job_create"),
    path("detail/<pk>", JobDetailView.as_view(), name="job_detail"),
    path("update/<pk>", JobUpdateView.as_view(), name="job_update"),
    path("delete/<pk>", JobDeleteView.as_view(), name="job_delete"),

]