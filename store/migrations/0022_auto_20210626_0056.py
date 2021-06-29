# Generated by Django 3.1.4 on 2021-06-25 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_all_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_orders',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.order'),
        ),
        migrations.AlterField(
            model_name='all_orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='all_orders',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
