# Generated by Django 3.1.4 on 2021-04-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210421_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=2, upload_to='uploads/products/'),
            preserve_default=False,
        ),
    ]
