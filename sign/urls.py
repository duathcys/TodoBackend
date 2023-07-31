from django.urls import path

from .views import user_login, user_signUp, find_id

urlpatterns = [
    path("login/", user_login),
    path("signup/", user_signUp),
    path("find/id/", find_id)
]