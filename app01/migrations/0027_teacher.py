# Generated by Django 2.1.2 on 2018-11-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0026_auto_20181107_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=32)),
                ('cid', models.ManyToManyField(to='app01.Class0')),
            ],
        ),
    ]
