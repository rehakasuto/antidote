# Generated by Django 4.2.2 on 2023-06-21 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0008_alter_license_license_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="license",
            name="license_key",
            field=models.CharField(
                default=uuid.UUID("543d2202-c697-4b16-8926-12bf72f88ef2"),
                max_length=50,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="license",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                unique=True,
            ),
        ),
    ]
