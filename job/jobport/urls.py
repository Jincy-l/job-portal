

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("",views.index,name='index'),
    path("index",views.index,name='index'),
    path("about",views.about,name='about'),
   
    path("error",views.error,name='error'),
    path("jobdetail",views.jobdetail,name='jobdetail'),
    path("joblist",views.joblist,name='joblist'),
    path("testimonial",views.testimonial,name='testimonial'),
    path("contact",views.contact,name='contact'),
    path("login",views.login,name='login'),
    path("employerlogin",views.employerlogin,name='employerlogin'),
    path("employe",views.employe,name='employe'),
    path("regemplr",views.regemplr,name='regemplr'),
    path("regemp",views.regemp,name='regemp'),
    path("otpempr",views.otpempr,name='otpempr'),
    path("profileemlr",views.profileemlr,name='profileemlr'),
    path("postajob",views.postajobs,name='postajob'),
    path("logout",views.logout,name='logout'),
    path("profileemp",views.profileemp,name='profileemp'),
    path("applyjob",views.applyjob,name='applyjob'),
    path("Applied",views.Applied,name='Applied'),
    path("profile",views.profile,name="profile"),
    # path("Resume",views.Resume,name='Resume'),
    # path("search",views.search,name='search'),
    path("myjobs",views.myjobs,name='myjobs'),
    path("approvedlist",views.approvedlist,name='approvedlist'),
    path("rejected",views.rejected,name='rejected'),
    path('approvecandidate/<int:applicationid>/', views.approvecandidate, name='approvecandidate'),
    path("rejectcandidate/<int:applicationid>/",views.rejectcandidate,name='rejectcandidate'),
    path('view_resume/<int:profile_id>/', views.view_resume, name='view_resume'),
    path("",views.indexadmin,name='indexadmin'),
    path("indexadmin",views.indexadmin,name='indexadmin'),
    path('accountadmin',views.accountadmin,name='accountadmin'),
    path('chartsadmin',views.chartsadmin,name='chartsadmin'),
    path('docsadmin',views.docsadmin,name='docsadmin'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('resetpassword',views.resetpassword,name='resetpassword'),
    path('indextable',views.indextable,name='indextable'),
    path('emptable',views.emptable,name='emptable'),
    path('deletedata/<int:id>',views.deletedata,name='deletedata'),
    path('signupadmin',views.signupadmin,name='signupadmin'),
    path('search_job',views.search_job,name='search_job'),
    path('message',views.message,name='message'),
    path('msgemp',views.msgemp,name='msgemp'),
    path('ordersadmin',views.ordersadmin,name='ordersadmin'),
    # path('updateprofile',views.updateprofile,name='updateprofile'),

    path('profile/', views.profileemp, name='profileemp'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('settingsadmin',views.settingsadmin,name='settingsadmin'),
    

    


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)