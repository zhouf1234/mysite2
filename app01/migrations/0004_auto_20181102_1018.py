# Generated by Django 2.1.2 on 2018-11-02 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
