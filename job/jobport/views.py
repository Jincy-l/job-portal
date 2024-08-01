from django.shortcuts import render,redirect
from . models import *
import random
# import PyPDF2
# from PyPDF2 import PdfReader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.core.mail import settings,send_mail,EmailMessage
from django.template.loader import render_to_string
from django.http import FileResponse
from django.contrib import messages
# Create your views here.





# Create your views here.
def index(request):
    sample_jobs = postajob.objects.order_by('?')[:5]
    jobs=postajob.objects.all()
    context={
        'jobs':jobs,
        'sample_jobs':sample_jobs
    }
    

    try:
        email= request.session['email']
        if employer.objects.filter(email=email).exists():
            image=employer.objects.filter(email=email)
            for i in image:
                img = i.image
            context={
                'email':email,
                'image':img,
                'jobs':jobs,
                'sample_jobs':sample_jobs,
                'employer':True
            } 
        else:
            image=employee.objects.filter(email=email)
            for i in image:
                img = i.image
            context={
                'email':email,
                'image':img,
                'jobs':jobs,
                'sample_jobs':sample_jobs,
                'employee':True
            } 

         

            print(sample_jobs)      

        return render(request,"index.html",context)
    except:
        return render(request,"index.html",context)

def error(request):
    return render(request,"error.html")
def about(request):
    return render(request,"about.html")

def contact(request):
    try:
        email= request.session['email']
        t=''
        if employee.objects.filter(email=email).exists():
            t='employee'
        else:
            t='employer'
        if request.method=="POST":
            name = request.POST['name']
            email=request.POST['email']
            message=request.POST['msg']

            msg(name=name,email=email,message=message,type=t).save()
            
        return render(request,"contact.html",{'email':email})
    except:
        return render(request,"contact.html")

def jobdetail(request):
    #  jobs= postajob.objects.get(id=id)
     jobs=postajob.objects.all()
     context={
        'jobs':jobs,
     }


     return render(request,"jobdetail.html",context)
def joblist(request):
    jobs=postajob.objects.all()
    context={
        'jobs':jobs,
    }

    return render(request,"joblist.html",context)
def testimonial(request):
    return render(request,"testimonial.html")

def login(request):
    return render(request,"login.html")

def employerlogin(request):
     if request.method == "POST":
        
        mail = request.POST['email']
        pswd = request.POST['password']
        
        user = employer.objects.filter(email = mail, password = pswd)

        if  employee.objects.filter(email = mail, password = pswd).exists():
            messages.error(request, 'user not an employer')
            return redirect('employerlogin')
        
        if user.exists():
            for i in user:
                com=i.company
                request.session['com']=com
            request.session['email'] = mail
            employer.objects.filter(email = mail, password = pswd).update()
            return redirect("index")
       
        else:
            super_admin=authenticate(username=mail,password=pswd)
            

            if super_admin is not None:
                if super_admin.is_superuser:
                    return redirect(indexadmin)
            else:

                messages.error(request, 'invalid credintiols')
                return redirect('employerlogin')
            
        
        
     return render(request,"employerlogin.html")    

def employe(request):
      if request.method == "POST":
        
        mail = request.POST['email']
        pswd = request.POST['password']
        
        user = employee.objects.filter(email = mail, password = pswd)

        if  employer.objects.filter(email = mail, password = pswd).exists():
            messages.error(request, 'user not an employee')
            return redirect('employe')


        

        
        if user.exists():
            request.session['email'] = mail
            employee.objects.filter(email = mail, password = pswd).update()
            return redirect("index")
       
        else:
            messages.error(request, 'invalid credintiols')
            return redirect('employerlogin')
        
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
        position=request.POST['position']
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
     if employee.objects.filter(email =email).exists():
        registrations = employee.objects.filter(email =email)
        context={
                'registrations':registrations,
            }
            
            
        return render(request,'profileemp.html',context)
     elif employer.objects.filter(email =email).exists():
         
        registrations = employer.objects.filter(email =email)
        context={
                'registrations':registrations,
            }
            
            
        return render(request,'profileemlr.html',context)



def profileemlr(request):
       
        
        return render(request,'profileemlr.html')
    
    
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
        jobid=request.POST['jobtitle']
        print(email,jobid,name)
    #    userid=int(userid)

 
        try:
            user=employee.objects.get(email=email)
            apply.objects.create(applicant=user,name=name,jobid=jobid,email=email)

            return redirect('index')
        except employee.DoesNotExist:
            return redirect('index')

               






        return redirect(index) 
     
def Applied(request):
    email = request.session['email']
    com=request.session['com']
    print(email)
    job=apply.objects.filter(name=com,approved=False,rejected=False)

    context={
        'job':job
    }
     
    return render (request,"Applied.html",context)
def myjobs(request):
    email = request.session['email']
    print(email)
    job=apply.objects.filter(email=email)
    context={
        'job':job
    }
    return render(request,"myjobs.html",context)


# Function to extract text from PDF
# def Resume(request):
#     pdf_path = 'C:/Users/Lenovo/OneDrive/Desktop/resumejincy.pdf'

#     # Open the PDF file
#     if pdf_path.startswith('file:'):
#         pdf_path = pdf_path[5:]  # Remove 'file:'
    
#     # Open and read the PDF file
#     reader = PdfReader(pdf_path)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text
        
# def search(request):
#     search=None
#     query=None
#     if 'q' in request.GET:
#         query=request.GET.get('q')
#         postajob.objects.all()
def approvedlist(request):
    email = request.session['email']
  
    approved_applications = apply.objects.filter(approved=True,email=email)

    
    return render(request, 'approvedlist.html', {'approved_applications': approved_applications})

def rejected(request):
    email = request.session['email']
    
    rejected_applications = apply.objects.filter(rejected=True,email=email)
    
    return render(request, 'rejected.html', {'rejected_applications': rejected_applications})

 

def approvecandidate(request,applicationid):
    try:
        job=apply.objects.get(id=applicationid)
        job.approved=True
        job.save()
        email = job.email  # Adjust this if your model has a different field name for email
        otp = random.randint(1000, 9999)
        subject = 'Application Approved'
        message = f'Your application has been approved. Your OTP is: {otp}'
        
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        # email=request.session['email']
        # send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
    
        return HttpResponse("Candidate approved Successfully.")
    except apply.DoesNotExist:
        return HttpResponse("Application not found")



    
        
    
    
    

def rejectcandidate(request,applicationid):
    try:
        job=apply.objects.get(id=applicationid)
        job.rejected=True
        job.save()
        return HttpResponse("Rejected")
    except apply.DoesNotExist:
        return HttpResponse("Application no found")
    

def view_resume(request, profile_id):
    
    pdf_file = employee.objects.get(id=profile_id)
    
    return FileResponse(pdf_file.resume, content_type='application/pdf')
def  indexadmin(request):
    empr=employer.objects.all()
    totalemployer=len(empr)
    emp=employee.objects.all()
    totalemployee=len(emp)
    sus=employee.objects.filter(sus=False)
    totalsus=len(sus)
    rsus=employer.objects.filter(sus=False)
    totalrsus=len(rsus)
    # email= request.session['email']
    # t=''
    # if employee.objects.filter(em=email).exists():
    #     t='employee'
    # else:
    #     t='employer'

    mess = msg.objects.all()
      
    context={
        'empr':empr,
        'totalemployer':totalemployer,
        'emp':emp,
        'totalemploye':totalemployee,
        'sus':sus,
        'totalsus':totalsus,
        'rsus':rsus,
        'totalrsus':totalrsus,
        'mess':mess,
        


    } 
    
  

    return render(request,'indexadmin.html',context)
def  accountadmin(request):
    return render(request,'accountadmin.html')
def  chartsadmin(request):
    return render(request,'chartsadmin.html')
def  docsadmin(request):
    return render(request,'docsadmin.html')
def ordersadmin(request):
    return render(request,'ordersadmin.html')
def  loginadmin(request):
    if request.method == "POST":
        
        mail = request.POST['email']
        pswd = request.POST['password']
        
        admin = adminn.objects.filter(email = mail, password = pswd)
        if admin.exists():
            for i in admin:
                 request.session['email'] = mail
            adminn.objects.filter(email = mail, password = pswd).update()
            return redirect("indexadmin")
       
        else:
           return redirect('loginadmin')

    return render(request,'loginadmin.html')
def  resetpassword(request):
    return render(request,'resetpassword.html')
def signupadmin(request):
    if request.method =="POST":
        name= request.POST['fullname']
        email= request.POST['email']
        password= request.POST['password']
        adminn( name=name,email=email, password=password ).save()


    return render(request,'signupadmin.html')
def indextable(request):

    
    empr=employer.objects.all()

    context={
        'empr':empr
    }
     
    return render (request,"indextable.html",context)

    
def emptable(request):
    emp=employee.objects.filter(sus=True)
    sus= employee.objects.filter(sus=False)
    context={
        'emp' :emp,
        'sus':sus
    }
    

    
    

    return render(request,'emptable.html',context)

def deletedata(request,id):
    
    de=employee.objects.get(id=id)
    de.sus=False
    de.save()
    email=de.email
    # otp = random.randint(1000, 9999)
    subject = 'Deleted account'
    message = f'Your account was deleted  '
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
    return redirect(emptable)
        
def search_job(request):
    if request.method=="POST":
        jobid=request.POST['jobtitle']
        jobtype=request.POST['full']
        city=request.POST['city']
        print(jobid,jobtype,city)
        jobs=postajob.objects.filter(jobtitle=jobid,jobtype=jobtype,city=city)
        print(jobs,'===================================')
        context={
            'jobs':jobs
        }
        return render(request,'search_jobs.html',context)


    return redirect(index)      
def message(request):
    # mess = msg.objects.all()
    mess= msg.objects.filter(type='employer')
    context={
        'mess':mess,
    }
    return render(request,'message.html',context)

       
def msgemp(request):
     mess= msg.objects.filter(type='employee')
    # mess = msg.objects.all()
     context={
        'mess':mess,
    }

     return render(request,'msgemp.html',context)
def updateprofile(request):
    
    if request.method=='POST': 
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        position=request.POST['position']
        company=request.POST['company']
        street=request.POST['street']
       
        pin=request.POST['zip']
        
        code=request.POST['zip']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        password=request.POST['password']
        # confirm=request.POST['confirm']
        # image=request.POST['photo']
        
        
        email = request.session['email'] 
        employer.objects.filter(email=email).update(firstname= firstname, lastname = lastname, position = position, company = company, street=street,   code=code, password = password,phonenumber=phonenumber,email=email)
       
    return redirect(profileemlr)