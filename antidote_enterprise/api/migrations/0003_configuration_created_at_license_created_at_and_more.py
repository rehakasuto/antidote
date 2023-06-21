# Generated by Django 4.2.2 on 2023-06-13 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_provideruser_wallet_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="configuration",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 13, 21, 51, 59, 585592)
            ),
        ),
        migrations.AddField(
            model_name="license",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 13, 21, 51, 59, 585592)
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 13, 21, 51, 59, 584452)
            ),
        ),
        migrations.AddField(
            model_name="provideruser",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 13, 21, 51, 59, 584452)
            ),
        ),
    ]