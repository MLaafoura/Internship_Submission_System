# Generated by Django 4.1.7 on 2023-05-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0068_alter_internshipform_sgk_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='officiallet',
            name='transcript',
            field=models.FileField(default='None', upload_to='transcript/'),
        ),
    ]