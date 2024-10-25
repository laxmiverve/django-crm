from django.urls import path, include
from .views import *


urlpatterns = [
    path("", home, name = "home"),
    path("register/", register_user, name = "register"),
    path("logout/", logout_user, name = "logout"),
    path("record/<int:pk>", user_record, name = "record"),
    path("add_record", add_record, name = "add_record"),
    path("delete_record/<int:pk>", delete_record, name = "delete_record"),
    path("update_record/<int:pk>", update_record, name = "update_record"),
]