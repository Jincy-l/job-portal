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
    

    try:
        email= request.session['email']
        if employer.objects.filter(email=email).exists():
            image=employer.objects.filter(email=email)
        else:
            image=employee.objects.filter(email=email)

        for i in image:
            img = i.image
            context={
                'email':email,
                'image':img,
                'jobs':jobs,
            }        

        return render(request,"index.html",context)
    except:
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
      if request.method == "POST":
        
        mail = request.POST['email']
        pswd = request.POST['password']
        
        user = employee.objects.filter(email = mail, password = pswd)
        
        if user.exists():
            request.session['email'] = mail
            employee.objects.filter(email = mail, password = pswd).update()
            return redirect("index")
       
        else:
            return redirect('employe')
        
      return render(request,"employe.html")


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
        position=request.POST['postion']
        print(Name)
        print(company)
        image = request.FILES.get('photo')

            
        employer(firstname = Name, lastname = lastname, company = company, street = street, addimfor = additional,
                  code = code, phonenumber = phone, email = email, password=password,  confirm=Confirm,
                  pin=pin,image=image,place=place,position=position).save()
        
        otp = random.randint(1000, 9999)
        print(otp)
        subject='project'
        message=str(otp)
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)

        return redirect('otpempr')
        
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
        city=request.POST['city']
        country=request.POST['country']
        code=request.POST['code']
        phonenumber=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        con=request.POST['confirm']
        resume = request.FILES.get('resume')
        image = request.FILES.get('photo')


        
        employee(firstname=firstname,lastname=lastname,Street=street,Pin=pin,skills=skills,
                highqua=highqua,job=job,city=city,country=country,code=code,phonenumber=phonenumber,
                email=email,password=password,con=con ,resume=resume,image=image).save()
        return redirect(employe)
    
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
     

def profileemp(request):
     email = request.session['email']
     print(email)
     registrations = employee.objects.filter(email =email)
     context={
            'registrations':registrations,
        }
        
        
     return render(request,'profileemp.html',context)



def profileemlr(request):
        email = request.session['email']
        registrations = employer.objects.filter(email = email)
        context={
            'registrations':registrations,
        }
        
        return render(request,'profileemlr.html',context)
    
    
def profile(request):
    
    try:
        email = request.session['email']
        
        if employee.objects.filter(email=email).exists():
            user_profile = employee.objects.filter(email=email)
            context = {
                ' registrations': user_profile
            }
            return render(request, 'profileemp.html', context)
        
        elif employer.objects.filter(email=email).exists():
            emp_profile = employer.objects.filter(email=email)
            context = {
                'registrations': emp_profile
            }
            return render(request, 'profileemlr.html', context)
        else:
            return redirect("index") 

    except:
        return redirect("index")
    


# def edit(request):
#     if request.method == 'POST':
        
#         Firstname = request.POST['firstname']
#         Lastname = request.POST['lastname']
#         Address = request.POST['address']
#         Country = request.POST['country']
    
    
#         Pincode = request.POST['pincode']
#         Phone = request.POST['phone']
#         Email = request.POST['email']
#         Password = request.POST['pswd']
#         code=request.POST['code']

#         user_type = request.session.get('employee')

#         if user_type == 'employee':
            
#             Qualification = request.POST['qua']
#             skills = request.POST['skills']
#             Resume = request.FILES.get('resume')
#             street=request.POST["street"]

#             Email = request.session['email']
            
#             employee.objects.filter(email=Email).update(
#                 first_name=Firstname, last_name=Lastname, highqua=Qualification, skills=skills,
#                 resume=Resume, address=Address, country=Country, street=street, pincode=Pincode,
#                  phone=Phone, email=Email, password=Password,code=code)
            

#         elif user_type == 'employer':
            
#             Position = request.POST['position']
#             Company = request.POST['company']
#             addimfor = request.POST['additional']

#             Email = request.session['email']
            
#             employer.objects.filter(email=Email).update(
#                 first_name=Firstname, last_name=Lastname, position=Position, company=Company, addimfor=addimfor,
#                 address=Address, country=Country, code=code, pincode=Pincode, phonenumber=Phone,
#                 email=Email, password=Password)
            

#         return redirect(profile)



def postajobs(request):
    
    if request.method=="POST":
        mail=request.session['email']
        location = request.POST['place']
        city= request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        
        jobtitle = request.POST['Jobtitle']
        des = request.POST['des']
        jobtype = request.POST['Full']
        qua = request.POST['qua']
        schedule = request.POST['schedule']
        num = request.POST['num']
        company=request.POST['company']
        pay=request.POST['pay']
        image = request.FILES.get('photo')
    
        
        postajob( image=image,location = location, city = city, state =state,  pincode = pincode, jobtitle = jobtitle, jobdes = des, jobtype=jobtype,  quali=qua,schedule=schedule,numberof=num,mail=mail,company=company,pay=pay).save()
    
    
    return render(request,'postajobs.html')

def logout(request):
    
    if 'email' in request.session:
        email = request.session['email']
        
        del request.session['email']
        
        employer.objects.filter(email = email).update() 
        
    return redirect('index')




def applyjob(request):
     
     if request.method=="POST":
       
       
       
       email=request.session['email']

       name=request.POST['company']
    #    userid=request.POST['jobid']
       jobid=request.POST['Jobtitle']
    #    userid=int(userid)

       if email and name:
           try:
              user=employee.objects.get(email=email)
              apply.objects.create(applicant=user,name=name)

              return redirect(index)
           except employee.DoesNotExist:
               return redirect(index)

               



    #    apply(name=name,userid=userids,jobid=jobid).save()


       return redirect(index) 
     
def Applied(request):
    email = request.session['email']
    print(email)
    job=apply.objects.filter()
    return render (request,"Applied.html")