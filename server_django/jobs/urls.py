# import these two
from django.urls import path
from . import views

urlpatterns = [
    # now telling which function => which path(or route)
    path('', views.index),
    path('get_jobs', views.get_jobs, name = 'getJobs'),
    # now link this to main projects urls
    path('post_jobs', views.post_jobs, name = 'postJobs')
]