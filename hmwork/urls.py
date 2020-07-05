from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('hospital/add_patient',views.add_patient,name="add_patient"),
    path('hospital/add_doctor',views.add_doctor,name="add_doctor"),
    path('hospital/add_stap',views.add_stap,name="add_stap"),
    path('hospital/patient_datils',views.patient_detils,name="patient_detils"),
    path('hospital/stap_details', views.stap_details, name="stap_details"),
    path('hospital/doctor_details', views.doctor_details, name="doctor_details"),
    path('hospital/about',views.about,name="about"),
    path('hospital/login',views.login,name="login"),
    path('hospital/signup',views.signup,name="signup"),

    path('delete_doctor/<int:id>',views.delete_doctor,name="delete_doctor"),
    path('delete_patient/<int:id>',views.delete_patient,name="delete_patient"),
    path('delete_stap/<int:id>',views.delete_stap,name="delete_stap"),
    path('logout',views.logout,name="logout"),


]