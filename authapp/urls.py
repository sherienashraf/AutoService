from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('signup/',views.signup_request,name='signup'),
    
    
]