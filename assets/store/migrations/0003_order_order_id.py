# Generated by Django 4.2.1 on 2023-05-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_services_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]