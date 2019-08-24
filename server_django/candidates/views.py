from django.shortcuts import render
from .models import Candidate


# Create your views here.
def view_candidates(requests):
    context = {
        "candidates" : Candidate.objects.all()
    }
    return render(requests, "candidates.html", context)


def post_candidates(requests):
    if requests.method == "data":
        job_id = int(requests.POST['jobid'])
        job_title = requests.POST['jobtitle']
        email = requests.POST['email']
        name = requests.POST['name']
        j = Candidate(jobid = job_id, jobtitle = job_title, email = email, name = name)
        j.save()
        return True