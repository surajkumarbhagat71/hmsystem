from django import forms
from .models import *

class Hospitalfrom(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'


class Pasentform(forms.ModelForm):
    class Meta:
        model = Pasent
        exclude = ('date_time','hospital_id',)



class Dform(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ('data_time','hospital_id',)


class Sform(forms.ModelForm):
    class Meta:
        model = Stap
        exclude = ('data_time','hospital_id',)