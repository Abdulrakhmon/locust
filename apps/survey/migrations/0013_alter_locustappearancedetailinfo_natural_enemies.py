# Generated by Django 4.0.5 on 2022-07-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0012_alter_locustappearancedetailinfo_natural_enemies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locustappearancedetailinfo',
            name='natural_enemies',
            field=models.ManyToManyField(blank=True, related_name='+', to='survey.naturalenemy'),
        ),
    ]
