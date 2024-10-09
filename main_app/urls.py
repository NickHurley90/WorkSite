from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/', views.job_listings, name='job_listings'),
    path('jobs/<int:listing_id>/', views.job_detail, name='job_detail'),
    path('jobs/<int:listing_id>/register/', views.register_for_job, name='register_for_job'),
    path('create-job/', views.create_job_listing, name='create_job_listing'),
    path('employer/register/', views.employer_register, name='employer_register'),
    path('staff/register/', views.staff_register, name='staff_register'),
    path('signup/', views.signup, name='signup'),
    path('register/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
]