from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from studentpanel.forms import student_dataform
from studentpanel.models import student_data,fees
from django.http import HttpResponse

@login_required
def index_view(request):
    return render(request, 'index.html')

@login_required
def bursar_view(request):
    return render(request,'bursar.html')

def base_view(request):
    return render(request,'base.html')

def dashboard_view(request):
    return render(request,'dashboard.html')

def student_data_view(request):
     message=''
     if request.method=="POST":
            std_dataform = student_dataform(request.POST)
            if std_dataform.is_valid():
             std_dataform.save()
             message= "student added successfully"
            else:
                 std_dataform = student_dataform()
                 std_data = student_data.objects.all()  
                 context = {
                 'form': std_dataform,
                 'msg': message,
                 'std_data': std_data,
              }
            return render(request,"new student.html",context)
        
     def edit_student_view(request,std_id):
          student_data = student_data.objects.get(id=std_id)

          if request.method == "POST":
             std_dataform = student_dataform(request.POST, instance=student_data)
           
          if  std_dataform.is_valid():
            std_dataform.save()
            std_dataform = student_dataform( instance=student_data)
            message = "Changes saved Successfully!"  
    
         
          else:
              message = "Form has Invalid data" 
                
                    
          
     context = {
                'form' : std_dataform,
                'std_data': std_data,
                
                    }
     return render(request, 'edit student.html' ,context)

     
             
def delete_student_view(request, std_id):
        student_data = student_data.objects.get(id=std_id)

        student_data.delete()

        return redirect(student_data_view)
   
def sign_up_view(request):
              if request.method == "POST":
                 sign_up_form = UserCreationForm(request.POST)
          
                 if sign_up_form.is_valid():
                  sign_up_form.save()
                 message = 'User created Successfully'
              else:
                 message = 'Something went wrong'    
              return render(request,'registration/sign_up.html' )


                 
