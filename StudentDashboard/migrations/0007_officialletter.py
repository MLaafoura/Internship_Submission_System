# Generated by Django 4.1.7 on 2023-05-06 02:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0006_delete_coordinators'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficialLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=100)),
                ('CompanyName', models.CharField(max_length=255)),
                ('CoordinatorName', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
