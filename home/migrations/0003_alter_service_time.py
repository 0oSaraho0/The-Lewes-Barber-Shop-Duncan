# Generated by Django 4.2 on 2023-05-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_service_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service", name="time", field=models.IntegerField(default=45),
        ),
    ]
