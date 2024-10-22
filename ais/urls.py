from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter
from .views import StudentsViewSet

router = DefaultRouter() # Membuat router DRF
router.register(r'students', StudentsViewSet) # Menyambungkan StudentsViewSet ke URL /students/

urlpatterns = [
    path('about', views.about),
    path('', views.homepage),
    path('api/', include(router.urls)), # Ini akan menambahkan semua URL yang dibutuhkan untuk API
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