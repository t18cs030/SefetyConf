from django.urls import path
from .views import IndexView,AddView,EmergencyListView,EmployeeListView,SendView,TestSendView,ResultView

app_name='SafetyConf'
urlpatterns = [
    path('',IndexView.as_view(),name='Index'),
    path('add',AddView.as_view(),name='Add'),
    path('EmergencyList',EmergencyListView.as_view(),name='EmergencyList'),
    path('EmployeeList',EmployeeListView.as_view(),name='EmployeeList'),
    path('Send',SendView.as_view(),name='Send'),
    path('TestSend',TestSendView.as_view(),name='TestSend'),
    path('Result',ResultView.as_view(),name='Result')
]


