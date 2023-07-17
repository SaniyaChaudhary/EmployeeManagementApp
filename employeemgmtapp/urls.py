from django.contrib import admin
from django.urls import path ,include
from .views import *
urlpatterns = [
    path('home/', emp_home),
    path('addemp/',add_emp),
    path("delete_emp/<int:empId>",delete_emp),
    path("update_emp/<int:empId>",update_emp),
    path("do_update_emp/<int:empId>",do_update_emp),
    path("testimonials/",testimonials),
    path("feedback/",feedback),
]


 