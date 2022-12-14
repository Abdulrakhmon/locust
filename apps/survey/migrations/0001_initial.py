# Generated by Django 4.0.5 on 2022-06-24 01:41

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0003_alter_user_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biotope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Биотоп',
                'db_table': 'biotope',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='Locust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha_code', models.CharField(max_length=8, unique=True)),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('description_uz', models.TextField()),
                ('description_en', models.TextField()),
                ('description_ru', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Саранча',
                'db_table': 'locust',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='LocustAge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Возраст личинок',
                'db_table': 'locust_age',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='LocustAppearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Присутствуют Саранчовые',
                'db_table': 'locust_appearance',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='LocustStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Саранча',
                'db_table': 'locust_stage',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory_name', models.CharField(max_length=256)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
                ('surveyed_area_in_ha', models.DecimalField(decimal_places=4, max_digits=10)),
                ('temperature', models.CharField(max_length=8)),
                ('wind', models.CharField(max_length=8)),
                ('damaged_area_in_ha', models.DecimalField(decimal_places=4, max_digits=10)),
                ('note', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Сохранено'), (2, 'Одобренный')], default=1)),
                ('approved_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agronomist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to=settings.AUTH_USER_MODEL)),
                ('biotope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.biotope')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='common.district')),
                ('locust_appearance', models.ManyToManyField(related_name='+', to='survey.locustappearance')),
                ('locusts', models.ManyToManyField(related_name='+', to='survey.locust')),
            ],
            options={
                'verbose_name': 'Обследования саранчи',
                'db_table': 'survey',
            },
        ),
        migrations.CreateModel(
            name='Vegetation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Растительность',
                'db_table': 'vegetation',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='VegetationCover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Густота растительного покрова',
                'db_table': 'vegetation_cover',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='SurveyAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='survey/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='survey.survey')),
            ],
            options={
                'db_table': 'survey_album',
            },
        ),
        migrations.CreateModel(
            name='SurveyAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11)),
                ('given_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agronomist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_acts', to=settings.AUTH_USER_MODEL)),
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
            options={
                'db_table': 'survey_act',
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='survey',
            name='vegetation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.vegetation'),
        ),
        migrations.AddField(
            model_name='survey',
            name='vegetation_cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.vegetationcover'),
        ),
        migrations.CreateModel(
            name='LocustAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='locust/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('locust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='survey.locust')),
            ],
            options={
                'verbose_name': 'Альбом саранчи',
                'db_table': 'locust_album',
            },
        ),
        migrations.AddIndex(
            model_name='surveyact',
            index=models.Index(fields=['number'], name='survey_act_number_216938_idx'),
        ),
        migrations.AddIndex(
            model_name='surveyact',
            index=models.Index(fields=['given_date'], name='survey_act_given_d_5b7d1c_idx'),
        ),
        migrations.AddIndex(
            model_name='survey',
            index=models.Index(fields=['approved_at'], name='survey_approve_54f4f1_idx'),
        ),
    ]
