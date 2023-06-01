from django.shortcuts import render
from django.views.generic import ListView  , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from StudentDashboard.models import InternshipForm , Opportunities 
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from StudentDashboard.models import Opportunities

class SgkRequests(LoginRequiredMixin , ListView):
    template_name ="CareerCenter.html"
    model = InternshipForm
    context_object_name = "approvedrequests"
    paginate_by = 10
    def get_queryset(self):
        stat = "Approved"
        queryset = super().get_queryset().filter(Status=stat)
        return queryset
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            
            # Count occurrences of each choice category
            context['done_count'] = self.get_queryset().filter(SGK_Status='Done').count()
            context['sgk_wait'] = self.get_queryset().filter(SGK_Status='Waiting For Approval').count()

            queryset = self.get_queryset()
            paginator = Paginator(queryset, self.paginate_by)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            context['page_obj'] = page_obj
            return context

class CreateOpportunity(LoginRequiredMixin , CreateView ):
    model = Opportunities
    template_name = "NewOpportunities.html"
    fields =['title' , 'description' , 'link']
    success_url = reverse_lazy('newopportunities')

    def form_valid(self, form):
        messages.success(self.request, 'The Opportunity Submitted Successfully.')
        return super().form_valid(form)
    
class SubmitSGK(LoginRequiredMixin , UpdateView):
    template_name = "UploadSGK.html"
    model = InternshipForm
    context_object_name = "sgkd"
    fields=['SGK_File' , 'SGK_Status','SGKNotification']
    success_url = reverse_lazy("careerCenter")
    def form_valid(self, form):
        messages.success(self.request, 'Your File is Uploaded.')
        return super().form_valid(form)
    
class ListOpportunities(LoginRequiredMixin , ListView):
     model = Opportunities
     template_name ="AllOpportunities.html"
     context_object_name = "oppo"

class UpdateOpportunitites(LoginRequiredMixin , UpdateView):
     model = Opportunities
     template_name = "UpdateInternship.html"
     context_object_name = "Updopp"
     fields = ['title' , 'description','link']
     success_url = reverse_lazy('listopp')

class DeleteOpp(LoginRequiredMixin , DeleteView):
     model = Opportunities
     template_name = "ConfirmDeleteopp.html"
     context_object_name = "del"
     success_url = reverse_lazy('listopp')