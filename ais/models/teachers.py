from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Teachers(models.Model):
    nip = models.CharField(max_length=20, unique=True)  # NIP, usually a string
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.name

# Signal to create a User when a Teacher is created
@receiver(post_save, sender=Teachers)
def create_user_for_teacher(sender, instance, created, **kwargs):
    if created:
        # Create the corresponding User
        user = User.objects.create_user(
            username=instance.nip,  # Use NIP as username
            email=instance.email,
            password=instance.nip  # Set a default password or handle password input
        )
        # Add user to the 'Teacher' group
        teacher_group, _ = Group.objects.get_or_create(name='Teacher')
        user.groups.add(teacher_group)

# class Students(models.Model):
#     nim = models.CharField(max_length=20, unique=True)  # NIM, usually a string
#     name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255, unique=True)
#     phone_number = models.CharField(max_length=13, unique=True)
#     year = models.IntegerField()  # Tahun angkatan atau tahun masuk
#     teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)  # Relasi ke tabel Teachers

#     def __str__(self):
#         return self.name

# # Signal to create a User when a Student is created
# @receiver(post_save, sender=Students)
# def create_user_for_student(sender, instance, created, **kwargs):
#     if created:
#         # Create the corresponding User
#         user = User.objects.create_user(
#             username=instance.nim,  # Use NIM as username
#             email=instance.email,
#             password=instance.nim  # Set a default password or handle password input
#         )
#         # Add user to the 'Student' group
#         student_group, _ = Group.objects.get_or_create(name='Student')
#         user.groups.add(student_group)