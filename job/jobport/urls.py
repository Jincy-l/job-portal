

from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    # path("index",views.index,name='index'),
    path("about",views.about,name='about'),
    path("category",views.category,name='category'),
    path("error",views.error,name='error'),
    path("jobdetail",views.jobdetail,name='jobdetail'),
    path("joblist",views.joblist,name='joblist'),
    path("testimonial",views.testimonial,name='testimonial'),
    # path("indexemp",views.indexemp,name='indexemp'),
    path("login",views.login,name='login'),
    # path ("loginemployer",views.loginemployer,name='loginemployer'),
    
]