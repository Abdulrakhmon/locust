# Generated by Django 4.0.5 on 2022-06-30 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_alter_locustappearancedetailinfo_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyact',
            name='survey',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='survey_act', to='survey.survey'),
        ),
    ]
