from django.db import models

    

    
class student_data(models.Model):
    GENDER_CHOICES=[("M","Male"),("F","Female"),]
    std_name= models.CharField(max_length=50)
    std_class=models.CharField(max_length=10)
    classteacher=models.CharField(max_length=50)
    std_gender= models.CharField(max_length=4,choices=GENDER_CHOICES)
    year_of_entry=models.CharField(max_length=20)
    date_of_birth=models.DateField(max_length=20,auto_now=False)
    parents_name=models.CharField(max_length=50)
    parents_residence=models.CharField(max_length=50)
    parents_contact=models.CharField(max_length=10)
    
    
    class teacher_data(models.Model):
      GENDER_CHOICES=[("M","Male"),("F","Female"),]
    teachers_name= models.CharField(max_length=50)
    teachers_classes=models.CharField(max_length=10)
    teachers_subjects=models.CharField(max_length=50)
    teachers_gender= models.CharField(max_length=4,choices=GENDER_CHOICES)
    year_of_entry=models.CharField(max_length=20)
    date_of_birth=models.DateField(max_length=20,auto_now=False)
    contact=models.CharField(max_length=10)
    email=models.EmailField(max_length=200)
    next_of_kin_name=models.CharField(max_length=50)
    next_of_kin_residence=models.CharField(max_length=50)
    next_of_kin_contact=models.CharField(max_length=10)
    salary=models.CharField(max_length=20)
        

class fees(models.Model):
       student_data= models.ForeignKey(student_data,on_delete=models.CASCADE,max_length=50)
       std_fees=models.CharField(max_length=30)
       cleared_fees=models.CharField(max_length=45)
       fees_balance=models.CharField(max_length=45)
       requirements=models.CharField(max_length=50)
    
     

