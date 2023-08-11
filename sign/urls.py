from django.urls import path

from .views import user_login, user_signUp, find_id, user_delete

urlpatterns = [
    path("login/", user_login),
    path("signup/", user_signUp),
    path("find/id/", find_id),
    # path("auth/<int:pk>", user_auth)
    path("auth/drop/", user_delete),

]