from django.urls import path
from .views import userRegistration, UserLogin,loginPage,userLogout,profilePage,signupPage
urlpatterns = [
    path("authentication/user/registration/",userRegistration),
    path("authentication/user/login/",UserLogin),
    path("login",loginPage),
    path("logout",userLogout),
    path("userprofile",profilePage),
    path("signup",signupPage)
]
