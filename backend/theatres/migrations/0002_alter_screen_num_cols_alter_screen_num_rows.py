# Generated by Django 5.1.2 on 2025-02-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='num_cols',
            field=models.PositiveSmallIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='screen',
            name='num_rows',
            field=models.PositiveSmallIntegerField(default=10),
        ),
    ]
