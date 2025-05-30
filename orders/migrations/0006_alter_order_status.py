# Generated by Django 5.2 on 2025-04-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_alter_order_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("New", "New"),
                    ("Cancelled", "Cancelled"),
                    ("Completed", "Completed"),
                    ("Accepted", "Accepted"),
                ],
                default="New",
                max_length=10,
            ),
        ),
    ]
