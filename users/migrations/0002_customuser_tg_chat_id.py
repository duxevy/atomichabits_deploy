# Generated by Django 5.2 on 2025-04-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                max_length=155,
                null=True,
                verbose_name="Telegram chat ID",
            ),
        ),
    ]
