from django.forms import ModelForm
from studentpanel.models import student_data

class student_dataform(ModelForm):
    class Meta:
        model = student_data
        fields = '__all__'
       
      
       