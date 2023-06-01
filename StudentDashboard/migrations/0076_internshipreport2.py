# Generated by Django 4.1.7 on 2023-05-30 06:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_rename_coordinator_student_coordinator'),
        ('StudentDashboard', '0075_internshipreport_internshipreport2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipReport2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InternshipReport2', models.FileField(default='None', upload_to='Documents/Reports/')),
                ('name', models.CharField(default='My Internship Report', max_length=255)),
                ('date_sent', models.DateField(default=django.utils.timezone.now)),
                ('is_uploaded', models.BooleanField(default=False)),
                ('Receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.coordinator')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
        ),
    ]