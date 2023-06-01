from django.urls import path 
from .views import  ShowMessages  , ShowRequest , OffLetterRequests , GenerateLetter , ViewMessage , DeleteMessage , CoordinatorSendMessage 
from .views import UpdateStatus  , RejectApplication
from .views import ShowOutgoingMessages
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', ShowRequest.as_view() ,name='CoordinatorDashboard'),
    path('Messages/', ShowMessages.as_view() , name='CoordinatorMessages'),
    path('OfficialLetter/', OffLetterRequests.as_view() , name='CoordinatorOffLetter'),
    path('GenerateLetter/<int:pk>/pdf/' , GenerateLetter.as_view(), name="generateoffletter"),
    path('ViewMessage/<int:pk>/' , ViewMessage.as_view(), name="viewallmessage"),
    path('DeleteMessage/<int:pk>' ,DeleteMessage.as_view(), name="deletemessage" ),
    path('SendMessage', CoordinatorSendMessage.as_view(),name="sendmessage"),
    path('OutgoingMessages/' , ShowOutgoingMessages.as_view(),name="outgoing"),
    path('UpdateStudent/<int:pk>/',UpdateStatus.as_view(),name="UpdateStatus"),
    path('Rejection/<int:pk>/', RejectApplication.as_view() , name="rejection"),
    path('logout/',LogoutView.as_view(next_page='../..'),name='logout'),
]