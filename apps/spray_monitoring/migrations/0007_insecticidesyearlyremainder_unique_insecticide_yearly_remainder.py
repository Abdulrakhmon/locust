# Generated by Django 4.0.5 on 2022-07-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spray_monitoring', '0006_alter_insecticidesyearlyremainder_year'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='insecticidesyearlyremainder',
            constraint=models.UniqueConstraint(fields=('insecticide', 'region', 'year'), name='unique_insecticide_yearly_remainder'),
        ),
    ]