# Generated by Django 4.1.7 on 2023-05-12 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0031_rename_student_officialletter_sender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='student',
            new_name='sender',
        ),
        migrations.RenameField(
            model_name='officialletter',
            old_name='sender',
            new_name='student',
        ),
    ]