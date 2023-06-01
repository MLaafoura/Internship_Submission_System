from typing import Any, Dict, Optional
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic.edit import CreateView 
from django.views.generic.detail import DetailView 
from django.views.generic import DeleteView
from login.models import Student , Coordinator
from .models import StudentSendMessages, InternshipForm , Opportunities , StudentReceiveMessages , InternshipReport 
from .models import OfficialLet
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.http import FileResponse



class TestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_student 

class StudentDetailView(LoginRequiredMixin,TestMixin,DetailView):
    model = Student
    template_name="Student.html"
    context_object_name = 'student'

class StudentDashboard(LoginRequiredMixin,TestMixin,TemplateView):
    template_name='Student.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.user.pk
        context['pk'] = pk
        return context



class StudentMessages(LoginRequiredMixin,ListView):
    model = Coordinator
    template_name = 'Messages.html'
    context_object_name = 'coordinators'

class OfficialLetter(LoginRequiredMixin,TestMixin,TemplateView):
    template_name='Studentoffletter.html'


class SendMessage(LoginRequiredMixin, CreateView):
    model = StudentSendMessages
    fields =['Subject','Message_content','Message_file']
    template_name = 'Messages.html'
    success_url = reverse_lazy('StudentDashboard')
    
    def form_valid(self, form):
        student = self.request.user.student
        coordinator = student.coordinator
        form.instance.Sender_id = student.pk
        form.instance.Receiver_id = coordinator.pk
        messages.success(self.request, 'Your message has been sent successfully.')
        return super().form_valid(form)
    


class OffLetter(LoginRequiredMixin, CreateView , ListView):
    model = OfficialLet
    fields =['CompanyName','NumOfincintern','transcript','transcript_status']
    template_name = 'Studentoffletter.html'
    success_url = reverse_lazy('StudentDashboard')
    
    def form_valid(self, form):
        student = self.request.user.student
        coordinator = student.coordinator
        form.instance.student_id = student.pk
        form.instance.coordinator_id = coordinator.pk
        messages.success(self.request, 'Your request has been sent successfully.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = self.request.user
        context['generatedletter'] = OfficialLet.objects.filter(student__user=user)
        
        return context

class SubmitApplication(LoginRequiredMixin , CreateView):
    model = InternshipForm
    fields=['ApplicationForm','ApplicationFormUpload']
    template_name="Student.html"
    success_url = reverse_lazy('StudentDashboard')

    def form_valid(self, form):
        student = self.request.user.student
        coordinator = student.coordinator
        form.instance.sender_id = student.pk
        form.instance.Receiver_id = coordinator.pk
        messages.success(self.request, 'Your File is Uploaded.')
        return super().form_valid(form)

class ShowApplication(LoginRequiredMixin,ListView):
    model = InternshipForm
    template_name = 'Student.html'
    context_object_name = 'files'

    def get_queryset(self):
        student = self.request.user.student
        queryset = super().get_queryset().filter(sender_id=student)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.request.user.student  
        context['offletter'] = student.officiallet_set.all()
        context['report1'] = student.internshipreport_set.all()
        return context


def download_sgk(request, pk):
    sgk = get_object_or_404(InternshipForm, pk=pk)
    file_path = sgk.SGK_File.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)

class InternshipOpportunities(LoginRequiredMixin , ListView):
    template_name="Opportunities.html"
    model = Opportunities
    context_object_name="opp"

def download_letter(request, pk):
    letter = get_object_or_404(OfficialLet, pk=pk)
    file_path = letter.pdf_file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)

class SentMessages(LoginRequiredMixin , ListView):
    model = StudentSendMessages
    template_name ="Outgoing.html"
    context_object_name = "outgoings" 
    def get_queryset(self):
        student = self.request.user.student
        queryset = super().get_queryset().filter(Sender_id=student)
        return queryset
    
class ReceivedMessages(LoginRequiredMixin , ListView):
    model = StudentReceiveMessages
    template_name ="ReceivedMessages.html"
    context_object_name ="received"
    def get_queryset(self):
        student = self.request.user.student
        queryset = super().get_queryset().filter(Receiver_id=student)
        return queryset

class DeleteMessage(LoginRequiredMixin , DeleteView):
    model = StudentSendMessages
    template_name = "ConfirmDelete.html"
    success_url = reverse_lazy('sentm')

class DeleteIncomingMessage(LoginRequiredMixin , DeleteView):
    model = StudentReceiveMessages
    template_name = "ConfirmDelete.html" 
    success_url = reverse_lazy('receivedM')


class ShowOutgoing(LoginRequiredMixin , DetailView):
    model = StudentSendMessages
    template_name ="ShowMessage.html"
    context_object_name ="Omessage"

class ShowIncoming(LoginRequiredMixin , DetailView):
    model = StudentReceiveMessages
    template_name ="ShowMessage.html"
    context_object_name ="Omessage"

class SubmitReport(LoginRequiredMixin , CreateView):
    template_name="Student.html"
    fields=['InternshipReport','is_uploaded']
    model = InternshipReport
    success_url = reverse_lazy('StudentDashboard')

    def form_valid(self, form):
        student = self.request.user.student
        coordinator = student.coordinator
        form.instance.sender_id = student.pk
        form.instance.Receiver_id = coordinator.pk
        messages.success(self.request, 'Your File is Uploaded.')
        return super().form_valid(form)
    
