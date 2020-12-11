from django.db import models
from enum import unique

class Group(models.Model):
    groupId = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=30)

class Employee(models.Model):
    employeeId = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=30)
    mailaddress = models.EmailField()
    subMailaddress = models.EmailField(null=True,blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    
    
class EmergencyContact(models.Model):
    emergencyContactId = models.IntegerField(null=False,unique=True)
    destinationGroupe = models.ForeignKey(Group,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    deadline = models.DateTimeField()
    sendDate = models.DateTimeField()
    
class Answer(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    sendDate = models.DateTimeField()
    
    