from django.urls import path
from . import views

# app_name = 'authentication'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    # path('user/', views.UserProfileView.as_view(), name='dashboard-view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]