# Generated by Django 4.1 on 2023-01-05 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web_app", "0005_inference_market"),
    ]

    operations = [
        migrations.RemoveField(model_name="inference", name="kgv",),
        migrations.RemoveField(model_name="inference", name="market",),
        migrations.RemoveField(model_name="inference", name="mcap",),
    ]