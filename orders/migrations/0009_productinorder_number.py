# Generated by Django 2.0.6 on 2018-08-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180812_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinorder',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
