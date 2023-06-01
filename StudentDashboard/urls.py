from django.urls import path
from .views import StudentDashboard , StudentMessages   , SendMessage, OffLetter , StudentDetailView
from .views import SubmitApplication  , ShowApplication , InternshipOpportunities , ReceivedMessages , SentMessages
from django.contrib.auth.views import LogoutView
from .views import DeleteMessage , DeleteIncomingMessage , ShowOutgoing , ShowIncoming , SubmitReport 
from login.models import Student
from . import views
urlpatterns = [ 
    path('Messages/', SendMessage.as_view(), name='create'),
    path('createOfficialLetter/', OffLetter.as_view(), name='offletter'),
    path('UploadAppForm/' ,SubmitApplication.as_view(), name='appform'),
    path('' ,ShowApplication.as_view(), name='StudentDashboard'),
    path('', StudentDetailView.as_view() , name='StudentDashboard'),
    path('InternshipOpportunities/' , InternshipOpportunities.as_view(),name="InternOpportunities"),
    path('OutgoingMessages/' , SentMessages.as_view(), name="sentm"),
    path('download-letter/<int:pk>/', views.download_letter, name='download_letter'),
    path('downloadsgk/<int:pk>/', views.download_sgk , name='download_file'),
    path('ReceivedMessages/' , ReceivedMessages.as_view() , name="receivedM"),
    path('ConfirmDelete/<int:pk>/' , DeleteMessage.as_view() , name="deletem"),
    path('ConfirmDeletest/<int:pk>/' , DeleteIncomingMessage.as_view() , name="deletr"),
    path('ViewMessage/<int:pk>' , ShowOutgoing.as_view() , name="viewM") , 
    path('ViewIncoming/<int:pk>/' , ShowIncoming.as_view() , name="viewI"),
    path('UploadReport/', SubmitReport.as_view(), name="reportform"),
    path('logout/',LogoutView.as_view(next_page='../..'),name='logout'),

]