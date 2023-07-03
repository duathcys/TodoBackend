from django.urls import path

from .views import user_login, user_signUp, user_info

urlpatterns = [
    path("login/", user_login),
    path("signup/", user_signUp),
    path("info/", user_info)
]