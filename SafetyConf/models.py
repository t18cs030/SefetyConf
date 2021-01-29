from django.db import models
from enum import unique
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

class Group(models.Model):
    groupId = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=30,unique=True)
    
    def __str__(self):
        return self.name
    
    def getClass(self):
        return self.__class__.__name__

class Employee(models.Model):
    employeeId = models.BigIntegerField(null=False,unique=True,validators=[MinValueValidator(1), MaxValueValidator(9999999999)])
    name = models.CharField(max_length=30)
    mailaddress = models.EmailField(max_length=50)
    subMailaddress = models.EmailField(null=True,blank=True)
    group = models.ManyToManyField(Group)
    
    def __str__(self):
        return str(self.employeeId)+" "+self.name
    
    def getClass(self):
        return self.__class__.__name__

def checkDeadLine(value):
    if value < timezone.now():
        raise ValidationError("締切日は現在より先を設定してください。")

class EmergencyContact(models.Model):
    emergencyContactId = models.IntegerField(null=False,unique=True)
    destinationGroup = models.ManyToManyField(Group)
    title = models.CharField(max_length=30)
    text = models.TextField(null=True,blank=True)
    deadline = models.DateTimeField(validators=[checkDeadLine])
    sendDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.emergencyContactId)+" "+self.title
    
    def getClass(self):
        return self.__class__.__name__
    
    def getDeadLine(self,time=timezone.now()):
        return self.deadline > time
    
    def is_exist(self,emp):
        return Answer.objects.filter(emergencyContact=self,employee=emp).exists()

    def getEmployees(self):
        employees = set()
        for sendGroup in self.destinationGroup.all():
            for employee in Employee.objects.filter(group=sendGroup):
                employees.add(employee)
        return employees
    
    def getNoAnswerEmployees(self):
        employees = set()
        fullEmployees = self.getEmployees()
        for employee in fullEmployees:
            if not(self.is_exist(employee)):
                employees.add(employee)
        return employees
        
class Answer(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False)
    emergencyContact = models.ForeignKey(EmergencyContact,on_delete=models.CASCADE,null=False)
    answer1 = models.CharField(max_length=30)
    answer2 = models.CharField(max_length=30)
    sendDate = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True,blank=True)
    
    def getClass(self):
        return self.__class__.__name__
    
    def getDeadLine(self,time=timezone.now()):
        return self.emergencyContact.getDeadLine(time)
    
 
    
