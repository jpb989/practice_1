# Generated by Django 5.1.2 on 2024-12-03 10:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatres', '0002_alter_seat_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]