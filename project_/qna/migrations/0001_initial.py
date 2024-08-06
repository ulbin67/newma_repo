# Generated by Django 5.0.7 on 2024-08-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("postname", models.CharField(max_length=50)),
                ("mainphoto", models.ImageField(blank=True, null=True, upload_to="")),
                ("contents", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("answer", models.TextField(blank=True, null=True)),
                ("password", models.PositiveBigIntegerField()),
                ("is_faq", models.BooleanField(default=False)),
            ],
        ),
    ]