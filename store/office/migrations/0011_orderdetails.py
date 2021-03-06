# Generated by Django 3.1.6 on 2021-02-12 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0010_auto_20210211_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityordered', models.IntegerField()),
                ('price_each', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderedlinenumber', models.SmallIntegerField()),
                ('ordernumber', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='office.orders')),
                ('productcode', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='office.product')),
            ],
        ),
    ]
