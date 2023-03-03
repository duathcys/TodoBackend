from django.urls import path
from .views import todo_List
from .views import todo_Detail

urlpatterns = [
    path("list/", todo_List),
    path("list/<int:pk>", todo_Detail)
]