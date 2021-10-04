from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

from accounts.models import Employee, MyUser


class EmployeeForm(ModelForm):  # Employee form for registration
    """ Added an extra field for department for employee registration"""
    class Meta:
        model = Employee
        fields = ('department',)
