from django.urls import path
from .views import todo_List, check_todo
from .views import todo_Detail

urlpatterns = [
    path("list/", todo_List),
    path("list/<int:pk>", todo_Detail),
    path("list/update/<int:pk>", check_todo)
]