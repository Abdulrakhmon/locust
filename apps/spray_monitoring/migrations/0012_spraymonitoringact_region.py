# Generated by Django 4.0.5 on 2022-08-02 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_user_region'),
        ('spray_monitoring', '0011_insecticideexchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='spraymonitoringact',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.region'),
            preserve_default=False,
        ),
    ]
