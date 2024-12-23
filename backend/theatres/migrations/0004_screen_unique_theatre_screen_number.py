# Generated by Django 5.1.2 on 2024-12-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatres', '0003_alter_screen_id'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='screen',
            constraint=models.UniqueConstraint(fields=('theatre', 'screen_number'), name='unique_theatre_screen_number'),
        ),
    ]
