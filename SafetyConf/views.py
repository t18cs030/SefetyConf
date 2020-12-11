from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.template.backends.django import Template

class IndexView(TemplateView):
    template_name = "SafetyConf/SafetyConf_Index.html"
    
class AddView(TemplateView):
    template_name = "SafetyConf/SafetyConf_Add.html"
    
class EmergencyListView(TemplateView):
    template_name = "SafetyConf/SafetyConf_EmergencyList.html"
    
class SendView(TemplateView):
    template_name = "SafetyConf/SafetyConf_Send.html"
    
class EmployeeListView(TemplateView):
    template_name = "SafetyConf/SafetyConf_EmployeeList.html" 
    
class TestSendView(TemplateView):
    template_name = "SafetyConf/SafetyConf_TestSend.html"
    
class ResultView(TemplateView):
    template_name = "SafetyConf/SafetyConf_Result.html"
    
# Create your views here.
