# Generated by Django 2.1.2 on 2018-11-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_auto_20181104_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student1',
            name='cid',
            field=models.IntegerField(null=True),
        ),
    ]