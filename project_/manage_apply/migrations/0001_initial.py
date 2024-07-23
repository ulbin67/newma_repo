# Generated by Django 4.1 on 2024-07-23 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.CharField(max_length=10, null=True)),
                ('com_num', models.CharField(blank=True, max_length=11, null=True)),
                ('applicant', models.CharField(max_length=10, null=True)),
                ('apcan_phone', models.CharField(max_length=11, null=True)),
                ('address_num', models.CharField(max_length=5, null=True)),
                ('address_info', models.TextField(blank=True, null=True)),
                ('address_detail', models.TextField(blank=True, null=True)),
                ('deli_request', models.TextField(blank=True, null=True)),
                ('progress', models.CharField(choices=[(0, '박스 요청중'), (1, '박스 전송중'), (2, '박스 수거 요청중'), (3, '수거진행중'), (4, '수거완료')], default=0, max_length=2, null=True)),
                ('box_num', models.IntegerField(null=True)),
                ('invoice_numberaddress_num', models.TextField(null=True)),
            ],
        ),
    ]
