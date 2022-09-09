# Generated by Django 4.0.5 on 2022-07-20 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0020_alter_surveyact_given_date'),
        ('spray_monitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamageLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Поврежденность',
                'db_table': 'damage',
                'ordering': ['name_uz'],
            },
        ),
        migrations.CreateModel(
            name='VegetationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128, unique=True)),
                ('name_ru', models.CharField(max_length=128, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Растительность Тип',
                'db_table': 'vegetation_type',
                'ordering': ['name_uz'],
            },
        ),
        migrations.RemoveField(
            model_name='spraymonitoringact',
            name='vegetation',
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='adverse_effect_to_fumigator',
            field=models.BooleanField(default=False, verbose_name='Ish bajaruvchi behosdan insektisid tasiriga uchradimi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='atomizer_height_above_ground_in_m',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Purkashning yer yzuasidan balandligi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='average_speed_of_movement_in_km_s',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Harakatnign ortacha tezligi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='bands',
            field=models.BooleanField(default=False, verbose_name='Lichinkalar to`dasi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='barriers',
            field=models.BooleanField(default=False, verbose_name='Tosiq'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='damaged_area_in_ha',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Zararlangan maydon'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='density',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Zichligi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='distance_between_barriers_in_m',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='To`siq oraligi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='empty_containers_status',
            field=models.ManyToManyField(related_name='+', to='spray_monitoring.emptycontainersstatus', verbose_name='Bo`sh kontenyerlar'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='ending_at',
            field=models.DateTimeField(verbose_name='Ishlov berish tugallangan vaqt'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='given_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='infested_area_in_ha',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Tarqalgan maydon'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='is_clean_protective_clothing',
            field=models.BooleanField(default=True, verbose_name='Himoya kiyimi toza va yaxshi holatdami'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='is_effected_on_non_target_organisms',
            field=models.BooleanField(default=False, verbose_name='Boshqa organizimlarga tasiri'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='is_imago',
            field=models.BooleanField(default=False, verbose_name='Voyaga yetgan'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='length_of_barriers_in_m',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='To`siq uzunligi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='locust',
            field=models.ManyToManyField(related_name='+', to='survey.locust', verbose_name='Chigirtka turi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='locust_age',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.locustage', verbose_name='Lichinka yoshi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='locust_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='survey.locuststage', verbose_name='Rivojlanish bosqichi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='protective_clothing',
            field=models.ManyToManyField(related_name='+', to='spray_monitoring.protectiveclothing', verbose_name='Maxsus himoya vositalari'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='scattered',
            field=models.BooleanField(default=False, verbose_name='Mayda todalarga ajralish'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='sprayer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='spray_monitoring.sprayer', verbose_name='Purkagich'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='sprayer_model',
            field=models.CharField(max_length=128, verbose_name='Purkagich modeli'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='starting_at',
            field=models.DateTimeField(verbose_name='Ishlov berish boshlangan vaqt'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='swarms',
            field=models.BooleanField(default=False, verbose_name='To`dalar'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='temperature_at_beginning',
            field=models.CharField(max_length=8, verbose_name='Ishlov boshlangan davrdaki havo harorati'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='temperature_at_end',
            field=models.CharField(max_length=8, verbose_name='Ishlov tugagan davrdaki havo harorati'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='territory_name',
            field=models.CharField(max_length=256, verbose_name='Hudud yoki fermer xojalik nomi'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='treated_area_in_ha',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Ishlangan maydon'),
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='vegetation_height_in_sm',
            field=models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Osimliklar balandligi'),
        ),
        migrations.AddField(
            model_name='spraymonitoringact',
            name='vegetation_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='spray_monitoring.vegetationtype', verbose_name='O`simlik qoplami turi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spraymonitoringact',
            name='damage_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='spray_monitoring.damagelevel', verbose_name='Zararlanish darajasi'),
        ),
    ]