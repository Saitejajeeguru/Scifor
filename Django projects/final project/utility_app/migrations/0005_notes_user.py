# Generated by Django 5.0.3 on 2024-04-22 06:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility_app', '0004_notes_delete_note'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='new_notepad', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
