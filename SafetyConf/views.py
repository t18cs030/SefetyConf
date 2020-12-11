from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Employee,EmergencyContact
from django.template.backends.django import Template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from .forms import EmployeeIdForm, EmployeeForm,EmegencyContactForm
from django.core.mail import send_mail,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.conf import settings


class IndexView(TemplateView):
    template_name = "SafetyConf/SafetyConf_Index.html"
    
class AddView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_Add.html"
    model = Employee
    fields = ('employeeId', 'name', 'mailaddress', 'subMailaddress', 'group')
    success_url = 'Index/'
    
    def get_initial(self):
        minid=Employee.objects.all().aggregate(Max('employeeId'))['employeeId__max']
        if minid==None:
            minid=0
        return {'employeeId':minid+1}
    
class EmergencyListView(ListView):
    template_name = "SafetyConf/SafetyConf_EmergencyList.html" 
    model = EmergencyContact

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class SendView(CreateView):
    template_name = "SafetyConf/SafetyConf_Send.html"
    model = EmergencyContact
    fields = ['emergencyContactId','destinationGroupe','title','text','deadline','sendDate']
    success_url = 'Index/'
    
    def form_valid(self, form):
        subject = self.request.POST.get('title')
        message = self.request.POST.get('text')
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["mashi0433@gmail.com"]
        Email = EmailMessage(subject, message, from_email, recipient_list)
        Email.send()
        return super(SendView,self).form_valid(form)

    
class EmployeeListView(LoginRequiredMixin,ListView):

    template_name = "SafetyConf/SafetyConf_EmployeeList.html"
    model = Employee 

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TestSendView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_TestSend.html"

class ResultView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_Result.html"

# Create your views here.
