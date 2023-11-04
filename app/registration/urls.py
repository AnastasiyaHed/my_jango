from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.all_users, name='all_users'),
    path('user/<int:user_id>/', views.user_details, name='user_details'),
    path('registration_form/', views.registration_form, name='registration_form'),
    path('success/', views.success_page, name='success_page'),
]

