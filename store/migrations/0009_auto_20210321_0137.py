# Generated by Django 3.1.4 on 2021-03-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
