
from django.urls import path
from .views import home,login_user,register,logout_user
urlpatterns = [
    path('', home , name="home"),
    path("register", register, name="register"), 
    path("login_user", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
]
