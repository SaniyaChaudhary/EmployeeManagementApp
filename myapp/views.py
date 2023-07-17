from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    
    isActive=True
    if request.method=='POST':
         check=request.POST.get("check")
         print(check)  
         if check is  None: isActive=False
         else: isActive=True


    date=datetime.datetime.now()  
    name="Learn Django with Saniya"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'LUCKNOW'
    }
    # return HttpResponse("<h1>Hello this is index page  </h1> "+str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)

def about(request):

    print ("about function called from view")
    #return HttpResponse("<h1> Hello this is about page</h1>")
    return render (request,"about.html",{})

def services(request):

    print ("services function called from view")
    #return HttpResponse("<h1> Hello this is services page</h1>")
    return render (request,"services.html",{})
