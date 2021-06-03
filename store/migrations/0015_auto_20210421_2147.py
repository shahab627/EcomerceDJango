# Generated by Django 3.1.4 on 2021-04-21 16:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210401_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rating',
            field=models.IntegerField(default='0', null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]