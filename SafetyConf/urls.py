from django.urls import path
from .views import IndexView,AddView,EmergencyListView,EmployeeListView,SendView,TestSendView,ResultView
from django.contrib.auth import views as auth_views

app_name='SafetyConf'
urlpatterns = [
    path('index/',IndexView.as_view(),name='Index'),
    path('add/',AddView.as_view(),name='Add'),
    path('EmergencyList/',EmergencyListView.as_view(),name='EmergencyList'),
    path('EmployeeList/',EmployeeListView.as_view(),name='EmployeeList'),
    path('Send/',SendView.as_view(),name='Send'),
    path('TestSend/',TestSendView.as_view(),name='TestSend'),
    path('Result/',ResultView.as_view(),name='Result'),
    path('login/', auth_views.LoginView.as_view(template_name='SafetyConf/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
