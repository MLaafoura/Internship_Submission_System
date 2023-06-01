from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import  Student

class MyLogin(LoginView):
    redirect_authenticated_user = True
    template_name='loginform.html'
    def get_success_url(self):
        
        if self.request.user.is_student: 
                student = Student.objects.get(user=self.request.user)
                return reverse_lazy('StudentDashboard')
           
        if self.request.user.is_coordinator:
               return reverse_lazy('CoordinatorDashboard')
           
        if self.request.user.is_careercenter:
               return reverse_lazy('CareerCenterDashboard')
        

    def form_invalid(self, form):
        messages.error(self.request , 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))