# students/forms.py

from django import forms
from .models import LeaveRequeststaff

class LeaveRequeststaffForm(forms.ModelForm):
    class Meta:
        model = LeaveRequeststaff
        fields = [ 'reason']


###### attendance form for staff

from django import forms
from .models import StaffAttendanceRecord
from django.contrib.auth.models import User

class StaffAttendanceForm(forms.ModelForm):
    class Meta:
        model = StaffAttendanceRecord
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(StaffAttendanceForm, self).__init__(*args, **kwargs)
    #     self.fields['staff'].queryset = User.objects.filter(groups__name='STAFF')
