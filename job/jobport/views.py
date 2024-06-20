from django.shortcuts import render,redirect
from . models import *
import random

from django.core.mail import settings,send_mail,EmailMessage
from django.template.loader import render_to_string
# Create your views here.





# Create your views here.
def index(request):
    jobs=postajob.objects.all()
    context={
        'jobs':jobs
    }
    return render(request,"index.html",context)
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

def login(request):
    return render(request,"login.html")

def employerlogin(request):
     if request.method == "POST":
        
        mail = request.POST['email']
        pswd = request.POST['password']
        
        user = employer.objects.filter(email = mail, password = pswd)
        
        if user.exists():
            request.session['email'] = mail
            employer.objects.filter(email = mail, password = pswd).update()
            return redirect("index")
       
        else:
            return redirect('employerlogin')
        
     return render(request,"employerlogin.html")    

def employe(request):

    return render(request,'employe.html')

def regemplr(request):
     
     if request.method =="POST":
        Name = request.POST['firstname']
        lastname= request.POST['lastname']
        company = request.POST['company']
        business = request.POST['business']
        street = request.POST['street']
        additional = request.POST['additional']
        phone = request.POST['phone']
        place = request.POST['place']
        country = request.POST['country']
        code = request.POST['code']
        email = request.POST['email']
        password = request.POST['password']
        Confirm = request.POST['confirm']
        pin=request.POST['zip']
            
        employer(firstname = Name, lastname = lastname, company = company, street = street, addimfor = additional, code = code, phonenumber = phone, email = email, password=password,  confirm=Confirm,pin=pin).save()
        
     return render(request,'regemplr.html')

def regemp(request):
    if request.method=="POST":
     firstname=request.POST['firstname']
     lastname=request.POST['lastname']
     street=request.POST['street']
     pin=request.POST['zip']
     skills=request.POST['skills']
     highqua=request.POST['qua']
     job=request.POST['job']
     place=request.POST['place']
     country=request.POST['country']
     code=request.POST['code']
     phonenumber=request.POST['phone']
     email=request.POST['email']
     passworde=request.POST['password']
     con=request.POST['confirm']
     employee(first_name=firstname,last_name=lastname,Street=street,Pin=pin,skills=skills,highqua=highqua,job=job,place=place,country=country,code=code,phonenumber=phonenumber,email=email,passworde=passworde,con=con).save()
    return render(request,'regemp.html')
def otpempr(request):
     if request.method=='POST':
        email=request.POST['email']
        print(email)
        otp = random.randint(1000, 9999)
        print(otp)
        subject='project'
        message=str(otp)
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
    
        return render(request,'otpempr.html')
     
def profileemplr(request):
     mail = request.session['email'] 
     print(mail)

     if request.method =="POST":
        Name = request.POST['name']
        Father = request.POST['father_name']
        Address = request.POST['add']
        Gender = request.POST['gender']
        State = request.POST['state']
        City = request.POST['city']
        Phone = int(request.POST['number'])
        Pincode = int(request.POST['code'])
        Date = request.POST['date']
        Image = request.FILES.get('photo')
        File = request.FILES.get('file')
        Email = request.POST['email']
        Password = request.POST['password']
        Confirm = request.POST['confirm']
        
        employer(name = Name, fname = Father, address = Address, gender = Gender, state = State, city = City,  phone = Phone, pincode = Pincode, dob = Date, image = Image, file = File, email = Email, password = Password)

        registrations = employer.objects.filter(email = mail)
        for i in registrations:
         print(i.name)
        
        return render(request,'profileemplr.html',{'registrations': registrations})
    
    
def postajobs(request):
    
    if request.method=="POST":
        mail=request.session['email']
        location = request.POST['place']
        city= request.POST['city']
        Area = request.POST['Area']
        pincode = request.POST['pincode']
        address = request.POST['address']
        jobtitle = request.POST['Jobtitle']
        des = request.POST['des']
        jobtype = request.POST['Full']
        qua = request.POST['qua']
        schedule = request.POST['schedule']
        num = request.POST['num']
    
    
        
        postajob(location = location, city = city, area =Area, address = address, pincode = pincode, jobtitle = jobtitle, jobdes = des, jobtype=jobtype,  quali=qua,schedule=schedule,numberof=num,mail=mail).save()
    
    
        return render(request,'postajobs.html')
    return render(request,'postajobs.html')
