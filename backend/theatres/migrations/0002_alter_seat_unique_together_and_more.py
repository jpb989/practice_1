import theatres.models
import uuid
from django.db import migrations, models


def set_uuid_for_existing_rows(apps, schema_editor):
    Screen = apps.get_model("theatres", "Screen")
    for screen in Screen.objects.all():
        screen.id = uuid.uuid4()
        screen.save()


class Migration(migrations.Migration):

    dependencies = [
        ('theatres', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='screen',
            name='seat_capacity',
        ),
        migrations.AddField(
            model_name='screen',
            name='seating_grid',
            field=models.JSONField(default=theatres.models.default_grid),
        ),
        migrations.AddField(
            model_name='seat',
            name='column_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seat',
            name='row_name',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screen',
            name='new_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RunPython(set_uuid_for_existing_rows),
        migrations.RemoveField(
            model_name='screen',
            name='id',
        ),
        migrations.RenameField(
            model_name='screen',
            old_name='new_id',
            new_name='id',
        ),
        migrations.DeleteModel(
            name='ShowTime',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='is_vip',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='number',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='row',
        ),
    ]
