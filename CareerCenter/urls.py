from django.urls import path 
from .views import SgkRequests  , CreateOpportunity , SubmitSGK , ListOpportunities , UpdateOpportunitites , DeleteOpp
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',SgkRequests.as_view(),name="careercenter"),
    path('CareerCenter/',SgkRequests.as_view() , name="careerCenter"),
    path('NewOpportunities/', CreateOpportunity.as_view() , name="newopportunities"),
    path('UploadSGK/<int:pk>/',SubmitSGK.as_view() , name="uploadsgk"),
    path('AllOpportunities/' , ListOpportunities.as_view(), name="listopp"),
    path('UpdateOpportunity/<int:pk>', UpdateOpportunitites.as_view() , name="uptodate"),
    path('ConfirmDelete/<int:pk>/', DeleteOpp.as_view() , name="deleteopp"),
    path('logout/',LogoutView.as_view(next_page='../..'),name='logout'),

]