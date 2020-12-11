from django.contrib import admin

from SafetyConf.models import Employee,EmergencyContact,Answer,Group
admin.site.register(Employee)
admin.site.register(EmergencyContact)
admin.site.register(Answer)
admin.site.register(Group)
