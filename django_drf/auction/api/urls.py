
from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r"^login/$", views.LoginView.as_view()),
    re_path(r"^message/$", views.message.as_view()),
]
