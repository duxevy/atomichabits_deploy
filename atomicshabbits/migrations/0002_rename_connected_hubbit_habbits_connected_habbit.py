# Generated by Django 5.2 on 2025-04-13 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("atomicshabbits", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habbits",
            old_name="connected_hubbit",
            new_name="connected_habbit",
        ),
    ]
