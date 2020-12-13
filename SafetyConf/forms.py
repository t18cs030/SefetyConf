    
from django import forms
from .models import Employee,EmergencyContact,Answer
from random import choice
from pyexpat import model
# Create your forms here.

class EmployeeIdForm(forms.Form):
    employee_id = forms.IntegerField(label='ID')
    

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['employee','sendDate']
        
        
class ChoiceForm(forms.Form):
        Choice_1 = {
        ('無事','無事'),
        ('怪我','怪我')
        }
        Choice_2 = { 
        ('不可能','不可能'),
        ('出勤可能','出勤可能')            
            }
        answer_1 = forms.ChoiceField(label='本人',widget=forms.RadioSelect,choices=Choice_1)
        answer_2 = forms.ChoiceField(label='出勤',widget=forms.RadioSelect,choices=Choice_2)

            