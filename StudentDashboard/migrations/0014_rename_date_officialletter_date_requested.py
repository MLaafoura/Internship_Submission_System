# Generated by Django 4.1.7 on 2023-05-07 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0013_alter_studentsendmessages_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officialletter',
            old_name='date',
            new_name='date_requested',
        ),
    ]
