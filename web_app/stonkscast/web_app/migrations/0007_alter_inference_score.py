# Generated by Django 4.1 on 2023-01-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0006_remove_inference_kgv_remove_inference_market_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inference", name="score", field=models.FloatField(default=None),
        ),
    ]
