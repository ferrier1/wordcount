# Generated by Django 2.1.1 on 2018-10-13 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_word_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='count',
            new_name='number_of',
        ),
    ]
