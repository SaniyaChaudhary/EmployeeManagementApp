from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee, Testimonial
from .forms import FeedbackForm,EmpForm

# Create your views here.\
def emp_home(request):
    emps = Employee.objects.all()
    return render (request, "emp/home.html", {
        'emps' : emps
    })

def add_emp(request):
    if request.method=="POST":

        #data fetch

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_email = request.POST.get("emp_email")
        emp_working = request.POST.get("emp_working")

        #validate if you want here

        #create model obj and set the data

        e=Employee()
        
        return redirect ("/emp/home")
    form=EmpForm()
    form.save()
    return render (request,"emp/addemp.html", {'form':form})


def delete_emp(request, empId):
    emp=Employee.objects.get(pk=empId)
    emp.delete() 
    return redirect("/emp/home/")

def update_emp(request, empId):
    emp=Employee.objects.get(pk=empId)
    
    return render(request,"emp/update_emp.html",{
        'emp' : emp
    })


def do_update_emp(request, empId):

    if request.method =='POST':
        
        #data fetch

        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_email = request.POST.get("emp_email")
        emp_working = request.POST.get("emp_working")


        e=Employee.objects.get(pk=empId)

        e.name=emp_name
        e.empId=emp_id
        e.address=emp_address
        e.phone=emp_phone
        e.email=emp_email
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        #save the obj

        e.save()
    return redirect("/emp/home/")


def testimonials(request):
    testi=Testimonial.objects.all()

    return render(request, "emp/testimonials.html",{
        'testi':testi
    })


def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("data saved")
        else:
            return render(request, "emp/feedback.html",{'form':form})
    else:
        form=FeedbackForm()
        return render(request, "emp/feedback.html",{'form':form})






