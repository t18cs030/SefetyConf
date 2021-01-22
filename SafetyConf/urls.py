from django.urls import path
from .views import IndexView,AddView,EmergencyListView
from .views import EmployeeListView,SendView,TestSendView,ResultView,ChangeEmployeeView
from .views import AnswerView,ThanksView,AddGroupView
from . import views
from django.contrib.auth import views as auth_views

app_name='SafetyConf'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='SafetyConf/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('Index/',IndexView.as_view(),name='Index'),
    path('Add',AddView.as_view(),name='Add'),
    path('EmergencyList',EmergencyListView.as_view(),name='EmergencyList'),
    path('EmployeeList',EmployeeListView.as_view(),name='EmployeeList'),
    path('Send',SendView.as_view(),name='Send'),
    path('send/<int:id>', views.send, name='send'),
    path('TestSend',TestSendView.as_view(),name='TestSend'),
    path('Answer/<str:h>/<str:c>/',AnswerView.as_view(),name='Answer'),
    path('Thanks',ThanksView.as_view(),name='Thanks'),
    path('Result/<int:pk>',ResultView.as_view(),name='Result'),
    path('Change/<int:pk>',ChangeEmployeeView.as_view(),name='Change'),
    path('AddGroup',AddGroupView.as_view(),name='AddGroup'),
]


