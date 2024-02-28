from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.UserRegistration.as_view(), name='create-user'),
    path('user/', views.UserProfileView.as_view(), name='profile-view'),
    path('token/', views.CreateTokenView.as_view(), name='auth-token'),
    path('otp/', views.GenerateOtpView.as_view(), name='generate-otp'),
]