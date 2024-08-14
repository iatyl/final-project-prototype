# Generated by Django 4.2.6 on 2023-11-02 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_ircclient_name_alter_ircclient_sasl_login_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IRCEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("event_type", models.CharField(max_length=100)),
                ("event_source", models.CharField(max_length=200)),
                ("event_target", models.CharField(max_length=200)),
                ("event_arguments", models.JSONField(default=list)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.ircclient",
                    ),
                ),
            ],
        ),
    ]