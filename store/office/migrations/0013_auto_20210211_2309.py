# Generated by Django 3.1.6 on 2021-02-12 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0012_auto_20210211_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='customernumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.customers'),
        ),
    ]
