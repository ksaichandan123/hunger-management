# Generated by Django 4.2.6 on 2023-10-30 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodstore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_avaliable',
            new_name='is_availible',
        ),
    ]
