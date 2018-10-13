# Generated by Django 2.1.1 on 2018-10-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0005_auto_20181013_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashes',
            old_name='hash',
            new_name='word',
        ),
        migrations.AddField(
            model_name='word',
            name='hash',
            field=models.CharField(default='temphash', max_length=200),
            preserve_default=False,
        ),
    ]