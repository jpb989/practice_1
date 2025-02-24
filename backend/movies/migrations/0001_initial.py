# Generated by Django 5.1.2 on 2024-11-08 11:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('duration', models.PositiveIntegerField(help_text='Duration in minutes')),
                ('language', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('poster', models.ImageField(upload_to='movie_posters/')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
    ]
