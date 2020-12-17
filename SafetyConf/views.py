from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Employee,EmergencyContact,Answer
from django.template.backends.django import Template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from .forms import EmployeeIdForm,EmployeeForm,AnswerForm,ChoiceForm,MessageForm,EmergencyContactForm
from django.core.mail import send_mail,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.template.loader import render_to_string
import hashlib, zlib
import pickle
import urllib
from urllib import parse as parse
import base64

MY_SECRET = "TeamAFK"

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_Index.html"
    
class AddView(LoginRequiredMixin,CreateView):
    template_name = "SafetyConf/SafetyConf_Add.html"
    model = Employee
    form_class = EmployeeForm
    success_url = 'Index/'
    
    def get_initial(self):
        minid=Employee.objects.all().aggregate(Max('employeeId'))['employeeId__max']
        if minid==None:
            minid=0
        return {'employeeId':minid+1}
    
class EmergencyListView(LoginRequiredMixin,ListView):
    template_name = "SafetyConf/SafetyConf_EmergencyList.html" 
    model = EmergencyContact
    
class SendView(LoginRequiredMixin,CreateView):
    template_name = "SafetyConf/SafetyConf_Send.html"
    model = EmergencyContact
    form_class = EmergencyContactForm
    success_url = 'Index/'
    
    def form_valid(self, form):
        subject = self.request.POST.get('title')
        group = self.request.POST.get('destinationGroup')
        employees = Employee.objects.filter(group=group)
        from_email = settings.EMAIL_HOST_USER
        print(type(self.request))
        sentList=[]
        for employee in employees:
            if employee.mailaddress in sentList:
                continue
            else:
                sentList.append(employee.mailaddress)
            recipient_list = []
            recipient_list.append(employee.mailaddress) 
            data = [employee.employeeId,int(self.request.POST.get('emergencyContactId'))]
            m,code = self.encode_data(data)
            context = {
                        "name":employee.name,
                        "employeeId":employee.employeeId,
                        "deadline":self.request.POST.get('deadline'),
                        "text":self.request.POST.get('text'),
                        "m":m,
                        "code":code.decode(),
                        }
            message = render_to_string('SafetyConf/mails/main.txt', context)#self.request.POST.get('text')
            email = EmailMessage(subject,message, from_email, recipient_list)
            email.send()
        return super(SendView,self).form_valid(form)

    def get_initial(self):
        minid=EmergencyContact.objects.all().aggregate(Max('emergencyContactId'))['emergencyContactId__max']
        if minid==None:
            minid=0
        return {'emergencyContactId':minid+1}
    
    def encode_data(self,data):
        data.append(MY_SECRET)
        text = base64.b64encode(zlib.compress(pickle.dumps(data, 0)))
        m = hashlib.md5(text).hexdigest()[:12]
        return m, text
    
class EmployeeListView(LoginRequiredMixin,ListView):

    template_name = "SafetyConf/SafetyConf_EmployeeList.html"
    model = Employee 
    
class TestSendView(LoginRequiredMixin,CreateView):
    template_name = "SafetyConf/SafetyConf_TestSend.html"
    model = EmergencyContact
    form_class = EmergencyContactForm
    success_url = 'Index/'
    
    def post(self, request, *args, **kwargs):
        subject = self.request.POST.get('title')
        message = self.request.POST.get('text')
        group = self.request.POST.get('destinationGroup')
        employees = Employee.objects.filter(group=group)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = []
        bcc = []
        for em in employees:
            bcc.append(em.mailaddress) 
        email = EmailMessage(subject,message, from_email, recipient_list)
        email.send()
        return HttpResponseRedirect(reverse('SafetyConf:Index'))
    
    def get_initial(self):
        minid=EmergencyContact.objects.all().aggregate(Max('emergencyContactId'))['emergencyContactId__max']
        if minid==None:
            minid=0
        return {'emergencyContactId':minid+1}
    
class AnswerView(CreateView):
    template_name = "SafetyConf/SafetyConf_Answer.html"
    model = Answer
    form_class = AnswerForm 
    form_class2 = ChoiceForm
    form_class3 = MessageForm
    success_url = '../../Thanks'
        
    def form_valid(self, form):
        form2 = self.form_class2(self.request.POST)
        form3 = self.form_class3(self.request.POST)
        if form2.is_valid():
            reply1 = form2.cleaned_data['answer_1']
            reply2 = form2.cleaned_data['answer_2']
            form.instance.answer1 = reply1
            form.instance.answer2 = reply2
        if form3.is_valid():
            m = form3.data['message']
            form.instance.message = m
        return super(AnswerView,self).form_valid(form)
    
    def get_initial(self):
        hash = self.kwargs.get("hash")
        code = self.kwargs.get("code")
        data = self.decode_data(hash,code)
        initial = super().get_initial()
        initial["employee"]=Employee.objects.get(employeeId=data[0])
        return initial
        
    def get_context_data(self, **kwargs):
        hash = self.kwargs.get("hash")
        code = self.kwargs.get("code")
        data = self.decode_data(hash,code)
        context = super().get_context_data(**kwargs)
        context['choice'] = ChoiceForm()
        context['message'] = MessageForm()
        context["employeeId"] = data[0]
        context["emergencyContactId"]=data[1]
        context["hash"] = hash
        context["code"] = code
        print(data)
        return context
    
    def decode_data(self, hash, enc):
        m = hashlib.md5(enc.encode()).hexdigest()[:12]
        if m != hash:
            raise Exception("Bad hash!")
        data = pickle.loads(zlib.decompress(base64.b64decode(enc.encode())))
        if data[len(data)-1] != MY_SECRET:
            raise Exception("Bad hash!")
        del data[len(data)-1]
        return data
    
class ThanksView(TemplateView):
    template_name = "SafetyConf/SafetyConf_Thanks.html"    

class ResultView(ListView):
    template_name = "SafetyConf/SafetyConf_Result.html"
    model = Answer
# Create your views here.
    