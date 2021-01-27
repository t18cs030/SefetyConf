    
from django import forms
from .models import Employee,EmergencyContact,Answer,Group
from random import choice
from pyexpat import model
# Create your forms here.

class EmployeeIdForm(forms.Form):
    employee_id = forms.IntegerField(label='ID')
    
class EmployeeForm(forms.ModelForm):
    
    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group']=forms.ModelMultipleChoiceField(
            label="所属グループ",
            widget=forms.CheckboxSelectMultiple,
            queryset=Group.objects.all()
            )

    class Meta:
        model = Employee
        fields = ('employeeId', 'name', 'mailaddress', 'subMailaddress', 'group')
        labels = {
            'employeeId':'社員番号',
            'name':'名前',
            'mailaddress':'メールアドレス',
            'subMailaddress':'サブメールアドレス',
            'group':'所属'
            }
        
class ChangeEmployeeForm(forms.ModelForm):
    
    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["employeeId"].widget.attrs["readonly"]="readonly"
        self.fields['group']=forms.ModelMultipleChoiceField(
            label="所属グループ",
            widget=forms.CheckboxSelectMultiple,
            queryset=Group.objects.all()
            )

    class Meta:
        model = Employee
        fields = ('employeeId', 'name', 'mailaddress', 'subMailaddress', 'group')
        labels = {
            'employeeId':'社員番号',
            'name':'名前',
            'mailaddress':'メールアドレス',
            'subMailaddress':'サブメールアドレス',
            'group':'所属'
            }
        
class EmergencyContactForm(forms.ModelForm):
    
    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['destinationGroup']=forms.ModelMultipleChoiceField(
            label="宛先グループ",
            widget=forms.CheckboxSelectMultiple,
            queryset=Group.objects.all()
            )
        self.fields["emergencyContactId"].widget = forms.HiddenInput()
        self.fields["sendDate"].widget = forms.HiddenInput()
    
    class Meta:
        model = EmergencyContact
        fields = ('emergencyContactId','destinationGroup','title','text','deadline','sendDate')
        labels = {
            'emergencyContactId':'id',
            'destinationGroup':'所属',
            'title':'タイトル',
            'text':'内容',
            'deadline':'期限',
            'sendDate':'送信日'
            }
        
class AnswerForm(forms.ModelForm):
    
    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sendDate"].widget = forms.HiddenInput()
        self.fields["employee"].widget = forms.HiddenInput()
        self.fields["emergencyContact"].widget = forms.HiddenInput()
    
    class Meta:
        model = Answer
        fields = ['employee','sendDate',"emergencyContact"]
        labels = {
            'employee':'従業員',
            'sendDate':'送信日',
            'emergencyContact':'緊急連絡',
            }
           
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
        
class MessageForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['message']
        labels = {
            'message':'メッセージ',
            }
class GroupForm(forms.ModelForm):
    def __init__(self , *args , **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["groupId"].widget = forms.HiddenInput()
        
    class Meta:
        model = Group
        fields = ['groupId','name']
        labels = {
            'groupId':'ID',
            'name':'名前'
            }