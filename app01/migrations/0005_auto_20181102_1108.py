# Generated by Django 2.1.2 on 2018-11-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20181102_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
