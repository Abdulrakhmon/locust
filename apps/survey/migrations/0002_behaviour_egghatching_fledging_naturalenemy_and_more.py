# Generated by Django 4.0.5 on 2022-06-24 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Behaviour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Поведение',
                'db_table': 'behaviour',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='EggHatching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Отрождение',
                'db_table': 'egg_hatching',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='Fledging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Окрыление',
                'db_table': 'fledging',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='NaturalEnemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Естественные враги',
                'db_table': 'natural_enemy',
                'ordering': ['name_uz'],
            },
        ),
        migrations.AlterModelOptions(
            name='locuststage',
            options={'ordering': ['name_uz'], 'verbose_name': 'Фаза'},
        ),
        migrations.AlterModelTable(
            name='locustage',
            table='hopper_age',
        ),
        migrations.AlterModelTable(
            name='locuststage',
            table='hopper_stage',
        ),
        migrations.CreateModel(
            name='LocustAppearanceDetailInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('egg_pod_detected_area', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('egg_pod_density_from', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('egg_pod_density_to', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('average_number_of_eggs_in_pod', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('viability_of_eggs', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('adult_maturity', models.BooleanField(blank=True, null=True)),
                ('adult_density_from', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('adult_density_to', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('adult_feeding_and_roosting', models.BooleanField(blank=True, null=True)),
                ('adult_copulating', models.BooleanField(blank=True, null=True)),
                ('adult_laying', models.BooleanField(blank=True, null=True)),
                ('adult_flying', models.BooleanField(blank=True, null=True)),
                ('swarm_maturity', models.BooleanField(blank=True, null=True)),
                ('swarm_density', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('adult_fledging', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.fledging')),
                ('adult_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.locuststage')),
                ('behaviour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.behaviour')),
                ('egg_hatching', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.egghatching')),
                ('hopper_age', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.locustage')),
                ('hopper_age_in_band', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.locustage')),
                ('hopper_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.locuststage')),
                ('natural_enemies', models.ManyToManyField(blank=True, to='survey.naturalenemy')),
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
            options={
                'db_table': 'locust_appearance_detail_info',
            },
        ),
    ]
