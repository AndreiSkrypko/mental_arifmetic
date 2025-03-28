# Generated by Django 5.1.6 on 2025-03-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mental_app', '0002_rename_student_students_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='parent_first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='parent_last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='parent_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
