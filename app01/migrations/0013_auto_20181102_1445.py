# Generated by Django 2.1.2 on 2018-11-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_auto_20181102_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student2',
            name='cid',
            field=models.ForeignKey(default=1, on_delete=None, to='app01.Student'),
            preserve_default=False,
        ),
    ]
