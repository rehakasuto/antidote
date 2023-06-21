# Generated by Django 4.2.2 on 2023-06-21 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_configuration_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="configuration",
            name="provider_user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="api.provideruser",
                unique=True,
            ),
        ),
    ]
