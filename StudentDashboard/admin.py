from django.contrib import admin
from .models import StudentSendMessages , StudentReceiveMessages  , OfficialLet , InternshipForm , Opportunities ,InternshipReport
from login.models import Coordinator , Student 

admin.site.register(Coordinator)
admin.site.register(Student)
admin.site.register(StudentSendMessages)
admin.site.register(StudentReceiveMessages)
admin.site.register(OfficialLet)
admin.site.register(InternshipForm)
admin.site.register(Opportunities)
admin.site.register(InternshipReport)