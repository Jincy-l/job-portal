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
# def indexemp(request):
    # return render(request,"indexemp.html")
def login(request):
    return render(request,"login.html")
# def loginemployer(request):
    # return render(request,"loginemployer")
def employerlogin(request):
    return render(request,"employerlogin.html")    
def employee(request):
    return render(request,'employee.html')
def regemplr(request):
    return render(request,'regemplr.html')
def regemp(request):
    return render(request,'regemp.html')