# Generated by Django 2.1.2 on 2018-11-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]