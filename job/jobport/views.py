from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return redirect(request,"index.html"),
def error(request):
    return redirect(request,"error.html"),
def about(request):
    return redirect(request,"about.html"),
def category(request):
    return redirect(request,"category.html"),
def contact(request):
    return redirect(request,"contact.html"),
def jobdeatail(request):
    return redirect(request,"job-detail.html"),
def joblist(request):
    return redirect(request,"job-list.html"),
def testimonial(request):
    return redirect(request,"testimonial.html"),