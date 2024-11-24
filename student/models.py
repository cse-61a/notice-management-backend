from django.db import models

# Student model
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    @property
    def is_authenticated(self):
        return hasattr(self, 'customtoken')

    def __str__(self):
        return f"{self.name} ({self.student_id})"

# CustomToken model
class CustomToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='customtoken')

    def __str__(self):
        return f"Token for {self.student.name}"
