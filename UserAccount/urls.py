from django.urls import path, include
from UserAccount.views import RegisterAPIview, UserLoginAPIview, UserChangePasswordAPIview, ForgotPasswordToEmail


urlpatterns = [
    
    path('register/', RegisterAPIview.as_view()),
    path('login/', UserLoginAPIview.as_view()),
    path("user/change-password/", UserChangePasswordAPIview.as_view()),
    path("user/forgot-password/", ForgotPasswordToEmail.as_view()),
    
]
