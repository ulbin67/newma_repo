# Generated by Django 5.0.7 on 2024-07-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manage_apply", "0002_alter_apply_com_num"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apply",
            name="apcan_phone",
            field=models.CharField(max_length=14, null=True),
        ),
    ]
