# Generated by Django 4.1.7 on 2023-05-07 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0010_remove_studentsendmessages_receiver_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsendmessages',
            name='Student_id',
        ),
    ]