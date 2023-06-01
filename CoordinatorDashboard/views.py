from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.views.generic import TemplateView , DetailView , DeleteView , CreateView , UpdateView
from django.views.generic.list import ListView
from StudentDashboard.models import OfficialLet , InternshipForm , StudentSendMessages , StudentReceiveMessages
from django.contrib.auth.views import LoginView
from django_xhtml2pdf.views import PdfMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect 
from django.template.loader import render_to_string
from login.models import Student , Coordinator
from django.views.generic import View
import io
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.core.files import File
from django.http import FileResponse
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.core.paginator import Paginator
from django.db.models import F

from django.contrib.staticfiles import finders

class TestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_coordinator
    

class login(LoginView):
    redirect_authenticated_user = True 

class CoordinatorMessages(LoginRequiredMixin,TestMixin,TemplateView):
    template_name='CoordinatorMessages.html'

class CoordinatorOffLetter(LoginRequiredMixin,TestMixin,TemplateView):
    template_name='CoordinatorOffLetter.html'


class GenerateOffLetter(LoginRequiredMixin ,ListView):
    model = OfficialLet
    template = "officialLett.html"
    context_object_name = "students"

class ShowRequest(LoginRequiredMixin , ListView):
    model = InternshipForm
    template_name = "Coordinator.html"
    context_object_name = "Requests"
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Count occurrences of each choice category
        context['accepted_count'] = self.get_queryset().filter(Status='Approved').count()
        context['waiting_count'] = self.get_queryset().filter(Status='Waitng For Approval').count()
        context['cancelled_count'] = self.get_queryset().filter(Status='Rejected').count()

        # Enable pagination
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['page_obj'] = page_obj

        return context

class OffLetterRequests(LoginRequiredMixin , ListView):
    model = OfficialLet
    template_name = "CoordinatorOffLetter.html"
    context_object_name = "offrequests"


class GenerateLetter(LoginRequiredMixin , DetailView , PdfMixin , UpdateView):
    model = OfficialLet 
    template_name = "officialLett.html"
    
    def render_to_pdf(self, context):
        template = get_template(self.template_name)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8', link_callback=fetch_resources)

        if not pdf.err:
            student = self.get_object().student
            coordinator = self.request.user.coordinator
            official_let = OfficialLet(student=student, coordinator=coordinator)
            official_let.pdf_file.save('generated_letter.pdf', File(result))
            official_let.is_ready = True  # Set is_ready to True
            official_let.transcript_status = True  
            official_let.save(update_fields=['pdf_file', 'is_ready','transcript_status'])
            messages.success(self.request, 'Letter generated successfully.')
            return redirect('CoordinatorDashboard')

        return HttpResponse('Error generating PDF', status=500)


    def get(self, request, *args, **kwargs):
        student = self.get_object()
        context = {'Infos': student}

        pdf = self.render_to_pdf(context)
        if pdf:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="student_information.pdf"'
            response.write(pdf)

            return response

        return HttpResponse('Error generating PDF', status=500)

def fetch_resources(uri, rel):
    """
    Callback function for resolving static file URLs.
    """
    # Use the StaticFilesStorage to serve static files
    return StaticFilesStorage().url(uri)


class ShowMessages(LoginRequiredMixin , ListView):
    model = StudentSendMessages
    template_name = "CoordinatorMessages.html"
    context_object_name = "showmessages"

class ViewMessage(LoginRequiredMixin , DetailView):
    model = StudentSendMessages 
    template_name = "ViewMessage.html"
    context_object_name = "viwemessage"

class DeleteMessage(LoginRequiredMixin, DeleteView ):
    model = StudentSendMessages
    template_name="DeleteMessage.html"
    success_url = reverse_lazy('CoordinatorMessages')
    context_object_name ="deletemessage"


class CoordinatorSendMessage(LoginRequiredMixin , CreateView , ListView):
    model = StudentReceiveMessages
    template_name = "SendMessage.html"
    fields =['Receiver','subject','Message_content','Message_file']
    success_url = reverse_lazy('CoordinatorMessages')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context

    def form_valid(self, form):
        coordinator = self.request.user.coordinator
        form.instance.sender_id = coordinator.pk
        messages.success(self.request, 'Your message has been sent successfully.')
        return super().form_valid(form)
    
   
    

class ShowOutgoingMessages(LoginRequiredMixin, ListView):
    model = StudentReceiveMessages
    template_name = "outgoingmessages.html"
    context_object_name ="outgoings"

class UpdateStatus(LoginRequiredMixin , UpdateView):
    template_name ="Confirm.html"
    model = InternshipForm
    context_object_name = "studentchange"
    fields = ['Status','Notification']
    success_url = reverse_lazy('CoordinatorDashboard')
    def form_valid(self,form):
        self.request.Notification = "Your Application is Approved"
        self.request.Status = "Approved"
        messages.success(self.request, "The Status was updated successfully.")
        return super(UpdateStatus,self).form_valid(form)

class RejectApplication(LoginRequiredMixin, UpdateView):
    template_name = "reject.html"
    model = InternshipForm
    context_object_name = "studentreject"
    fields = ['Status','ApplicationFormUpload','Rejection_reason','Notification']
    success_url = reverse_lazy('CoordinatorDashboard')

    def form_valid(self, form):
        form.instance.Status = "Rejected"
        form.instance.ApplicationFormUpload = "0"
        form.instance.Rejection_reason = self.request.POST.get('Rejection_reason')
        messages.success(self.request, "The Status was updated successfully.")
        return super().form_valid(form)
    


class CoordinatorReply(LoginRequiredMixin,  CreateView):
    model = StudentReceiveMessages
    template_name="reply.html"
    context_object_name = "studentreply"
    fields =['Receiver','subject','Message_content','Message_file']
    success_url = reverse_lazy('CoordinatorMessages')
    
    def form_valid(self, form):
        coordinator = self.request.user.coordinator
        form.instance.sender_id = coordinator.pk
        messages.success(self.request, 'Your message has been sent successfully.')
        return super().form_valid(form)