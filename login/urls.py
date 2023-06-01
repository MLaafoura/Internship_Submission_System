from django.urls import path
from .views import MyLogin
from django.contrib.auth.views import LogoutView
from StudentDashboard.views import ShowApplication
from CoordinatorDashboard.views import ShowRequest
from CareerCenter.views import SgkRequests

urlpatterns = [
    path('', MyLogin.as_view(),name='login'),
    path('login/',MyLogin.as_view(),name='loginpr'),
    path('StudentDashboard/',ShowApplication.as_view() , name='StudentDashboard'),
    path('CoordinatorDashboard/',ShowRequest.as_view() , name='CoordinatorDashboard'),
    path('CareerCenter/',SgkRequests.as_view() , name='CareerCenterDashboard'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout')
]