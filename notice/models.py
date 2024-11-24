from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    NOTICE_TYPES = [
        ('assignment', 'Assignment'),
        ('lab_report', 'Lab Report'),
        ('class_test', 'Class Test'),
        ('presentation', 'Presentation'),
        ('exam', 'Exam'),
        ('classroom_code', 'Classroom Code'),
    ]

    description = models.TextField(blank=True, null=True)
    notice_type = models.CharField(max_length=50, choices=NOTICE_TYPES, blank=True, null=True)
    resource_link = models.URLField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='notices',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course} ({self.notice_type})"

