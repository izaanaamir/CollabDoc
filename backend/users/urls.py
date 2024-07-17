# In users/urls.py
from django.urls import path
from .views import (
    ChangePasswordView,
    UserRegistrationView,
    UserProfileView,
    LoginView,
    LogoutView,
    ForgotPasswordView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_register"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "change-password/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot_password",
    ),
]
