from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"index.html")
def error(request):
    return render(request,"error.html")
def about(request):
    return render(request,"about.html")
def category(request):
    return render(request,"category.html")
def contact(request):
    return render(request,"contact.html")
def jobdetail(request):
    return render(request,"jobdetail.html")
def joblist(request):
    return render(request,"joblist.html")
def testimonial(request):
    return render(request,"testimonial.html")