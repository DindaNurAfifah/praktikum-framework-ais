from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about),
    path('', views.homepage),
    path('student/', views.student_index, name='student_index'),
    path('student/create/', views.student_create, name='student_create'),# Create
]