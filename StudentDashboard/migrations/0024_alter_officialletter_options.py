# Generated by Django 4.1.7 on 2023-05-10 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0023_alter_officialletter_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='officialletter',
            options={'ordering': ['-date_requested'], 'verbose_name': 'OfficialLetter'},
        ),
    ]