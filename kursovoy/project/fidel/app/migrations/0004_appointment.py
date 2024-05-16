# Generated by Django 5.0.4 on 2024-05-15 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.master')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service')),
            ],
        ),
    ]