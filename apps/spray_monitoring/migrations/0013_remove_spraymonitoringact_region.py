# Generated by Django 4.0.5 on 2022-08-02 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spray_monitoring', '0012_spraymonitoringact_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spraymonitoringact',
            name='region',
        ),
    ]
