# Generated by Django 5.1.7 on 2025-04-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0005_alter_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount'),
        ),
    ]
