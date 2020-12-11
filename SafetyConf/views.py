from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Employee,EmergencyContact
from django.template.backends.django import Template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from .forms import EmployeeIdForm, EmployeeForm,EmegencyContactForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect

class IndexView(LoginRequiredMixin,TemplateView):
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
    
class EmergencyListView(LoginRequiredMixin,ListView):
    template_name = "SafetyConf/SafetyConf_EmergencyList.html" 
    model = EmergencyContact

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class SendView(LoginRequiredMixin,CreateView):
    template_name = "SafetyConf/SafetyConf_Send.html"
    model = EmergencyContact
    fields = ['emergencyContactId','destinationGroupe','title','text','deadline','sendDate']
    success_url = 'Index/'

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
