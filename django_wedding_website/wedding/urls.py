from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="wedding-register-form"),
    path("register/success/", views.success, name="wedding-register-success"),
]
