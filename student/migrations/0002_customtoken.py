# Generated by Django 5.1.3 on 2024-11-23 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
