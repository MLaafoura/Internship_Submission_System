# Generated by Django 4.1.7 on 2023-05-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0035_alter_files_applicationform_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='ApplicationForm',
            field=models.FileField(null=True, upload_to='Documents/'),
        ),
        migrations.AlterField(
            model_name='files',
            name='InternshipReport',
            field=models.FileField(null=True, upload_to='Documents/'),
        ),
    ]
