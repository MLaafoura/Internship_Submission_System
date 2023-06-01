from django.db import models    
from login.models import Student , Coordinator
from django.utils import timezone



class StudentSendMessages(models.Model):
    Subject = models.CharField(max_length=255)
    Sender = models.ForeignKey(Student , on_delete = models.CASCADE , null=True)
    Receiver = models.ForeignKey(Coordinator, on_delete=models.CASCADE,null=True)
    Message_content = models.CharField(max_length=1000)
    Message_file = models.FileField(upload_to='Documents/')
    date_sent = models.DateField(default=timezone.now)
    
    

class StudentReceiveMessages(models.Model):
    Receiver = models.ForeignKey(Student, on_delete=models.CASCADE)
    sender = models.ForeignKey(Coordinator, on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=255)
    Message_content = models.CharField(max_length=1000)
    Message_file = models.FileField(upload_to='Documents/' , null=True)
    date_received = models.DateField(default=timezone.now)
    def __str__(self):
        return self.Sender , self.subject , self.Message_content


class OfficialLet(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE  , primary_key=True)
    CompanyName = models.CharField(max_length=255)
    NumOfincintern = models.IntegerField()
    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE , null = True)
    date_requested = models.DateField(default=timezone.now)
    pdf_file = models.FileField(upload_to='Documents/officialletter/' , default="None")
    transcript = models.FileField(upload_to="transcript/" , default="None" )
    transcript_status = models.BooleanField(default=False)
    is_ready = models.BooleanField(default=False)

class InternshipForm(models.Model):
    FILE_STATUS = [
        ("Approved", "Approved"),
        ("Waitng For Approval", "Waiting For Approval"),
        ("Rejected", "Rejected"),
        ("Done","Done")
    ]
    sender = models.ForeignKey(Student, on_delete=models.CASCADE , null=True)
    Receiver = models.ForeignKey(Coordinator,on_delete=models.CASCADE, null=True)
    ApplicationForm = models.FileField(upload_to='static/Files', default='')
    name = models.CharField(max_length=255 , default="My Application Form")
    Status = models.CharField(max_length=255 , choices=FILE_STATUS , default="Waitng For Approval")
    date_sent = models.DateField(default=timezone.now)
    Rejection_reason = models.CharField(max_length=1000, default="")
    SGK_File = models.FileField(upload_to='sgkDocuments', default='')
    SGK_Status = models.CharField(max_length=255 , choices=FILE_STATUS , default="Waiting For Approval")
    ApplicationFormUpload = models.BooleanField(default=False)
    Notification = models.CharField(max_length=255, default="No updates")
    SGKNotification = models.CharField(max_length=255, null=True)

class InternshipReport(models.Model):
    sender = models.ForeignKey(Student, on_delete=models.CASCADE , null=True)
    Receiver = models.ForeignKey(Coordinator,on_delete=models.CASCADE, null=True)
    InternshipReport = models.FileField(upload_to='Documents/Reports/', default='None')
    InternshipReport2 = models.FileField(upload_to='Documents/Reports/', default='None')
    name = models.CharField(max_length=255 , default="My Internship Report")
    date_sent = models.DateField(default=timezone.now)
    is_uploaded = models.BooleanField(default=False)
    is_uploaded2 = models.BooleanField(default=False)

    
class Opportunities(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    link = models.CharField(max_length=100)
