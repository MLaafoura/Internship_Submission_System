# Generated by Django 4.1.7 on 2023-05-23 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDashboard', '0061_remove_opportunities_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sgkdocument',
            name='Status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Done', 'Done')], default='None', max_length=255),
        ),
    ]