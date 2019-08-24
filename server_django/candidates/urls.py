# import these two
from django.urls import path
from . import views

urlpatterns = [
    path('view_candidates', views.view_candidates, name = 'viewCandidates'),
    path('post_candidates', views.post_candidates, name = "postCandidates")
]

