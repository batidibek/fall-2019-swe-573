# Generated by Django 2.2.7 on 2019-11-17 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vircom', '0006_auto_20191117_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datatypeobject',
            name='fields',
        ),
    ]
