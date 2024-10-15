from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('about', views.about),
    path('', views.homepage),
    path('student/', views.student_index, name='student_index'),
    path('student/create/', views.student_create, name='student_create'),# Create
    path('student/update/<int:student_id>/', views.student_update, name='student_update'), #update
    path('student/delete/<int:student_id>', views.student_delete, name='student_delete'), #delete
    path('login/', auth_views.LoginView.as_view(), name='login'), #login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #logout
    path('dashboard/', views.dashboard, name='dashboard'), #dashboard
    path('dashboard/admin', views.dashboard_admin, name='dashboard_admin'), #dashboardAdmin
    path('dashboard/student', views.dashboard_student,name='dashboard_student'), #dashboardStudent
    path('dashboard/teacher', views.dashboard_teacher,name='dashboard_teacher'), #dashboardTeacher
]