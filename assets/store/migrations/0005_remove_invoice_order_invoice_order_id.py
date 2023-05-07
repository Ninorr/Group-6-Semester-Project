# Generated by Django 4.2.1 on 2023-05-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='order',
        ),
        migrations.AddField(
            model_name='invoice',
            name='order_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]