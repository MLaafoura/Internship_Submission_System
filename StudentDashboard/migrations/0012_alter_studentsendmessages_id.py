# Generated by Django 4.1.7 on 2023-05-07 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('StudentDashboard', '0011_remove_studentsendmessages_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsendmessages',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
