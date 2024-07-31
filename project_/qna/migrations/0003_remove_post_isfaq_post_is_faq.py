# Generated by Django 5.0.7 on 2024-07-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qna", "0002_rename_is_faq_post_isfaq"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="isfaq",
        ),
        migrations.AddField(
            model_name="post",
            name="is_faq",
            field=models.BooleanField(default=False),
        ),
    ]
