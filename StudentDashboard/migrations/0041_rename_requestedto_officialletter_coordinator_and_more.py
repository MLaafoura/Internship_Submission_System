# Generated by Django 4.1.7 on 2023-05-12 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0040_rename_student_id_officialletter_requestedfrom_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officialletter',
            old_name='requestedto',
            new_name='coordinator',
        ),
        migrations.RenameField(
            model_name='officialletter',
            old_name='requestedfrom',
            new_name='student',
        ),
    ]