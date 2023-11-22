
from django.contrib import admin
from django.urls import path,include
from studentpanel.views import index_view,bursar_view,base_view,dashboard_view,student_data_view,sign_up_view,delete_student_view,edit_student_view

urlpatterns = [
    path('admin/', admin.site.urls),
     path('index/',index_view,name='index_page'),
    path('bursar/',bursar_view,name='bursar_page'),
     path('',base_view,name='base_page'),
   path('dashboard',dashboard_view,name='dashboard_page'),
    path('new student/',student_data_view,name="new student_page"),
    path('',include("django.contrib.auth.urls")),
    path('edit_student/<int:std_id>/',edit_student_view,name='edit_student_page'),
     path('','sign_up/',sign_up_view,name='sign_up_page'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('delete_student/<int:std_id>/',delete_student_view, name="delete_student_page"),
]

