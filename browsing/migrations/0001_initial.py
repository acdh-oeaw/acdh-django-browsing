# Generated by Django 2.2.6 on 2019-12-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BrowsConf",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "model_name",
                    models.CharField(
                        blank=True,
                        help_text="The name of the model class you like to analyse.",
                        max_length=255,
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True,
                        help_text="The label of the value of interest.",
                        max_length=255,
                    ),
                ),
                (
                    "field_path",
                    models.CharField(
                        blank=True,
                        help_text="The constructor of to the value of interest.",
                        max_length=255,
                    ),
                ),
            ],
        ),
    ]
