# Generated by Django 2.1.2 on 2018-11-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20181101_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]
