# Generated by Django 2.1.2 on 2018-11-02 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20181102_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
    ]