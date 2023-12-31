# Generated by Django 4.2.2 on 2023-06-21 12:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_license_license_key_alter_license_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="license",
            name="license_key",
            field=models.CharField(
                default=uuid.UUID("2380dfce-e6d0-48e5-9496-c1051dd43d4a"),
                max_length=50,
                unique=True,
            ),
        ),
    ]
