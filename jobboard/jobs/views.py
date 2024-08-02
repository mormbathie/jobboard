from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import JobPost

def job_list(request):
    jobs = JobPost.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})
