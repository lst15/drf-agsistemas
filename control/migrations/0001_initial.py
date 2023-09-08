# Generated by Django 4.2.5 on 2023-09-05 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_departure_date', models.DateField()),
                ('control_departure_time', models.TimeField()),
                ('control_departure_km', models.PositiveIntegerField()),
                ('control_destination', models.CharField(max_length=200)),
                ('control_return_date', models.DateField(blank=True, null=True)),
                ('control_return_time', models.TimeField(blank=True, null=True)),
                ('control_return_km', models.PositiveIntegerField(blank=True, null=True)),
                ('control_distance_traveled', models.PositiveIntegerField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.driver')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
            options={
                'db_table': 'control',
            },
        ),
    ]