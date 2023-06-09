# Generated by Django 4.2 on 2023-05-10 10:28

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("product", models.CharField(max_length=300)),
                (
                    "description",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        force_format="WEBP",
                        keep_meta=True,
                        quality=75,
                        scale=None,
                        size=[400, None],
                        upload_to="products/",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
