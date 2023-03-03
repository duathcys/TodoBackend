from django.urls import path

from .views import user_login, user_signUp

urlpatterns = [
    path("login/", user_login),
    path("signup/", user_signUp)
]