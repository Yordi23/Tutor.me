# Generated by Django 2.1.11 on 2019-09-07 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190831_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_request',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 6, 21, 9, 28, 636872), verbose_name='Request date'),
        ),
    ]