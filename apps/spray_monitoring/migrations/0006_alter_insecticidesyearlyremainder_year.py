# Generated by Django 4.0.5 on 2022-07-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spray_monitoring', '0005_alter_insecticidesyearlyremainder_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insecticidesyearlyremainder',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
