# Generated by Django 4.1.7 on 2023-05-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_user_id_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='coordinator',
            table='login_coordinator',
        ),
    ]
