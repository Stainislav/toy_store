# Generated by Django 2.0.6 on 2018-11-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productimage_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
