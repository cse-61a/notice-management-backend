# Generated by Django 5.1.3 on 2024-11-23 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('notice_type', models.CharField(choices=[('assignment', 'Assignment'), ('lab_report', 'Lab Report'), ('class_test', 'Class Test'), ('presentation', 'Presentation'), ('exam', 'Exam'), ('others', 'Others')], max_length=50)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notices', to='notice.course')),
            ],
        ),
    ]
