# Generated by Django 2.1.11 on 2019-09-13 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190907_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutor',
            name='description',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_request',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 13, 0, 5, 8, 472592), verbose_name='Request date'),
        ),
    ]