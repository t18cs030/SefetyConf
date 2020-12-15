from django import forms
from .models import Employee,EmergencyContact
# Create your forms here.
class EmployeeIdForm(forms.Form):
    employee_id = forms.IntegerField(label='ID')
    
class EmployeeForm(forms.ModelForm):    
    class Meta:
        model = Employee
        fields = ['employeeId', 'name', 'mailaddress', 'subMailaddress', 'group']
        
class EmegencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['emergencyContactId','destinationGroupe','title','text','deadline','sendDate']
