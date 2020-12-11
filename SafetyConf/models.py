from django.db import models
from enum import unique

class Group(models.Model):
    groupId = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    employeeId = models.IntegerField(null=False,unique=True)
    name = models.CharField(max_length=30)
    mailaddress = models.EmailField()
    subMailaddress = models.EmailField(null=True,blank=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.employeeId)+" "+self.name

class EmergencyContact(models.Model):
    emergencyContactId = models.IntegerField(max_length=10,null=False,unique=True)
    destinationGroupe = models.ForeignKey(Group,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    deadline = models.DateTimeField()
    sendDate = models.DateTimeField()
    
    def __str__(self):
        return str(self.emergencyContactId)+" "+self.title
    
class Answer(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    sendDate = models.DateTimeField()
    
    