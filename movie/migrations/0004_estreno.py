# Generated by Django 4.1.4 on 2023-02-28 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_pelicula_director_pelicula_reparto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_estreno', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]