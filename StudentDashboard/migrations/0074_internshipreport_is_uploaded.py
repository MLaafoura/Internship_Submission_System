# Generated by Django 4.1.7 on 2023-05-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0073_officiallet_transcript_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipreport',
            name='is_uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
