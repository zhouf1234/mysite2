# Generated by Django 2.1.2 on 2018-11-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20181102_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=32, null=True)),
            ],
        ),
    ]
