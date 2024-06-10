from django.shortcuts import render,redirect
from . models import *

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
     if request.method =="POST":
        Name = request.POST['name']
        lastname= request.POST['lastname']
        company = request.POST['company']
        business = request.POST['business']
        street = request.POST['street']
        additional = request.POST['additional']
        phone = request.POST['phone']
        place = request.POST['place']
        country = request.POST['country']
        code = request.POST('code')
        
        email = request.POST['email']
        password = request.POST['password']
        Confirm = request.POST['confirm']
            
        employer(firstname = Name, lastname = lastname, company = company, street = street, addimfor = additional, pin = code, phonenumber = phone, email = email, password=password,  Confirm=Confirm).save()
        
     return render(request,'regemplr.html')
def regemp(request):
    return render(request,'regemp.html')