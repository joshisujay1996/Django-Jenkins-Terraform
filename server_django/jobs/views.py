
from django.shortcuts import render

# Import the models and the classes implemented there( indirectly means the table)
from .models import Job
# Create your views here.

# index page
def index(requests):
    return render(requests, 'index.html')

# get all posted jobs
def get_jobs(requests):
    context = {
        "jobs": Job.objects.all()
    }
    print(context['jobs'])
    return render(requests, 'get_jobs.html', context)

# pot new job 
def post_jobs(requests):
    if requests.method == "GET":
        return render(requests, 'post_jobs.html')
    if requests.method == "POST":
        job_id = int(requests.POST['jobid'])
        job_title = requests.POST['jobtitle']
        job_desscription = requests.POST['jobdescription']
        j = Job(jobid = job_id, jobtitle = job_title, jobdescription = job_desscription)
        j.save()
        return render(requests, "succes.html")
