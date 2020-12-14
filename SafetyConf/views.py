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
        message = self.request.POST.get('text')
        group = self.request.POST.get('destinationGroup')
        employees = Employee.objects.filter(group=group)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = []
        for employee in employees:
            recipient_list.append(employee.mailaddress) 
        send_mail(subject,message, from_email, recipient_list)
        return super(SendView,self).form_valid(form)

    def get_initial(self):
        minid=EmergencyContact.objects.all().aggregate(Max('emergencyContactId'))['emergencyContactId__max']
        if minid==None:
            minid=0
        return {'emergencyContactId':minid+1}
    
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
        for em in employees:
            recipient_list.append(em.mailaddress) 
        send_mail(subject,message, from_email, recipient_list)
        return HttpResponseRedirect(reverse('SafetyConf:Index'))
    
    def get_initial(self):
        minid=EmergencyContact.objects.all().aggregate(Max('emergencyContactId'))['emergencyContactId__max']
        if minid==None:
            minid=0
        return {'emergencyContactId':minid+1}
    
class AnswerView(LoginRequiredMixin,CreateView):
    template_name = "SafetyConf/SafetyConf_Answer.html"
    model = Answer
    form_class = AnswerForm 
    form_class2 = ChoiceForm
    form_class3 = MessageForm
    success_url = 'Thanks'
    
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
    

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choice'] = ChoiceForm()
        context['message'] = MessageForm()
        return context
    
class ThanksView(TemplateView):
    template_name = "SafetyConf/SafetyConf_Thanks.html"    

class ResultView(ListView):
    template_name = "SafetyConf/SafetyConf_Result.html"
    model = Answer
# Create your views here.
    