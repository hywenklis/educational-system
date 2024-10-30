from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.list_students, name='list_students'),
    path('courses/', views.list_courses, name='list_courses'),
]
