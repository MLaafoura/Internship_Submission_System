# Generated by Django 4.1.7 on 2023-05-10 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_coordinator_table'),
        ('StudentDashboard', '0014_rename_date_officialletter_date_requested'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsendmessages',
            name='Coordinator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.coordinator'),
        ),
    ]