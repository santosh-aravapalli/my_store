# Generated by Django 3.1.6 on 2021-02-12 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20210211_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='produdescription',
            new_name='productdescription',
        ),
    ]
