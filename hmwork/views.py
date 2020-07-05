from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

def home(r):


    return render(r, 'hospital/home.html')

def signup(r):
    form = Hospitalfrom(r.POST or None , r.FILES or None)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(login)

    data = {"signup":form}

    return render(r, 'hospital/signup.html',data)


def login(r):
    if r.method == "POST":
        email = r.POST.get('email')
        password = r.POST.get('password')

        cond = Q(email = email) & Q(password = password)

        cheak = Hospital.objects.filter(cond).count()

        if (cheak > 0 ):
            r.session['login'] = email
            return redirect(patient_detils)
        else:
            return redirect(login)

    return render(r, 'hospital/login.html')


def add_patient(r):
    if not r.session.has_key('login'):
        return redirect(login)

    form = Pasentform(r.POST or None , r.FILES or None)

    id = Hospital.objects.get(email=r.session['login']).h_id

    if r.method == "POST":
        if form.is_valid():
            a = form.save(commit=False)
            a.hospital_id = Hospital(id)
            a.save()
            return redirect(patient_detils)

    data = {"patient":form}

    return render(r,'hospital/add_patient.html',data)



def add_doctor(r):
    if not r.session.has_key('login'):
        return redirect(login)

    form = Dform(r.POST or None , r.FILES or None)

    id = Hospital.objects.get(email=r.session['login']).h_id

    if r.method == "POST":
        if form.is_valid():
            a = form.save(commit=False)
            a.hospital_id = Hospital(id)
            a.save()
            return redirect(patient_detils)

    data = {"doctor":form}

    return render(r,'hospital/add_doctor.html',data)


def add_stap(r):
    if not r.session.has_key('login'):
        return redirect(login)

    form = Sform(r.POST or None , r.FILES or None)

    id = Hospital.objects.get(email=r.session['login']).h_id

    if r.method == "POST":
        if form.is_valid():
            a = form.save(commit=False)
            a.hospital_id = Hospital(id)
            a.save()
            return redirect(patient_detils)

    data = {"stap":form}

    return render(r,'hospital/add_stap.html',data)



def patient_detils(r):
    if not r.session.has_key('login'):
        return redirect(login)

    id = Hospital.objects.get(email=r.session['login']).h_id

    data ={"patient":Pasent.objects.filter(hospital_id=id)}


    return render(r,'hospital/patient_detail.html',data)



def doctor_details(r):
    if not r.session.has_key('login'):
        return redirect(login)

    id = Hospital.objects.get(email=r.session['login']).h_id

    data = {"doctor":Doctor.objects.filter(hospital_id=id)}

    return render(r,'hospital/doctor_details.html',data)


def stap_details(r):
    if not r.session.has_key('login'):
        return redirect(login)

    id = Hospital.objects.get(email=r.session['login']).h_id

    data = {"stap": Stap.objects.filter(hospital_id=id)}

    return render(r, 'hospital/stap_details.html', data)


def about(r):

    return render(r,'hospital/about.html')


def delete_doctor(r,id):
    data = Doctor.objects.filter(d_id=id)
    data.delete()
    return redirect(doctor_details)


def delete_patient(r,id):
    data = Pasent.objects.filter(p_id=id)
    data.delete()
    return redirect(patient_detils)



def delete_stap(r,id):
    data = Stap.objects.filter(s_id=id)
    data.delete()
    return redirect(stap_details)


def logout(r):
    if r.session.has_key('login'):
        del r.session['login']
        return redirect(login)

    return render(r,'hospital/login.html')


