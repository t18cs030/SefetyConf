from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.template.backends.django import Template
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_Index.html"
    
class AddView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_Add.html"
    
class EmergencyListView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_EmergencyList.html"
    
class SendView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_Send.html"
    
class EmployeeListView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_EmployeeList.html" 

class TestSendView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_TestSend.html"

class ResultView(LoginRequiredMixin,TemplateView):
    template_name = "SafetyConf/SafetyConf_Result.html"

# Create your views here.
