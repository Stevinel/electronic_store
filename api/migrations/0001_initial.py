# Generated by Django 3.2.7 on 2021-09-18 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parameter",
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
                (
                    "title",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        verbose_name="Название параметра",
                    ),
                ),
            ],
            options={
                "verbose_name": "Параметр",
                "verbose_name_plural": "Параметры",
            },
        ),
        migrations.CreateModel(
            name="ParametersItem",
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
                (
                    "parameter_title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parameters",
                        to="api.parameter",
                        verbose_name="Параметры товара",
                    ),
                ),
            ],
            options={
                "verbose_name": "Параметр итем",
                "verbose_name_plural": "Параметр итемы",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "product_title",
                    models.CharField(max_length=50, verbose_name="Название"),
                ),
                (
                    "description",
                    models.CharField(max_length=3000, verbose_name="Описание"),
                ),
                (
                    "parameter",
                    models.ManyToManyField(
                        through="api.ParametersItem", to="api.Parameter"
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.AddField(
            model_name="parametersitem",
            name="product_title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_parameters",
                to="api.product",
                verbose_name="Название товара",
            ),
        ),
    ]
