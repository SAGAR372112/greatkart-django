# Generated by Django 5.2 on 2025-04-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status_remove_orderproduct_variations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('New', 'New'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]
