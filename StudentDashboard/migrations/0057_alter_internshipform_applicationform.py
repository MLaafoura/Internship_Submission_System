# Generated by Django 4.1.7 on 2023-05-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0056_remove_studentreceivemessages_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipform',
            name='ApplicationForm',
            field=models.FileField(default='None', upload_to='static/Files'),
        ),
    ]
