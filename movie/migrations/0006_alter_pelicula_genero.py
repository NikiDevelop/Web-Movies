# Generated by Django 4.0 on 2023-09-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_estreno_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.ManyToManyField(to='movie.Genero'),
        ),
    ]
