# Generated by Django 2.1.11 on 2019-08-31 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190831_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_request',
            old_name='tutor_id',
            new_name='tutor_ID',
        ),
        migrations.AlterField(
            model_name='user_request',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 31, 15, 10, 43, 879787), verbose_name='Request date'),
        ),
    ]
