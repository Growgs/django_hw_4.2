# Generated by Django 4.1.7 on 2023-06-10 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
