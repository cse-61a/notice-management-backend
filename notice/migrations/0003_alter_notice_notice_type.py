# Generated by Django 5.1.3 on 2024-11-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_notice_resource_link_alter_notice_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice_type',
            field=models.CharField(blank=True, choices=[('assignment', 'Assignment'), ('lab_report', 'Lab Report'), ('class_test', 'Class Test'), ('presentation', 'Presentation'), ('exam', 'Exam'), ('classroom_code', 'Classroom Code')], max_length=50, null=True),
        ),
    ]
