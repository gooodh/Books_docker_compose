# Generated by Django 4.2 on 2023-06-13 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_id_alter_book_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='uuid',
        ),
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
