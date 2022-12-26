from django.urls import path
from app2.views import *
app_name='anything2'
urlpatterns=[
    path('soumya/',soumya,name='soumya'),
    path('subash/',subash,name='subash'),
]