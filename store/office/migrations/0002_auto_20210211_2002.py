# Generated by Django 3.1.6 on 2021-02-12 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offices',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_instock',
            field=models.SmallIntegerField(),
        ),
    ]
