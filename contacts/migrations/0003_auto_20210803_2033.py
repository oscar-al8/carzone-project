# Generated by Django 3.1 on 2021-08-04 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210803_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 3, 20, 33, 45, 391916)),
        ),
    ]
