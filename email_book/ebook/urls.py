from django.urls import path
from ebook import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
]
