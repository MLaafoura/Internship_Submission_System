# Generated by Django 4.1.7 on 2023-05-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0072_internshipform_sgknotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='officiallet',
            name='transcript_status',
            field=models.BooleanField(default=False),
        ),
    ]
