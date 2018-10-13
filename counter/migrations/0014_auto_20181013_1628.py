# Generated by Django 2.1.1 on 2018-10-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0013_auto_20181013_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hash',
            name='word',
        ),
        migrations.AddField(
            model_name='word',
            name='hash',
            field=models.ForeignKey(default='7', on_delete=django.db.models.deletion.CASCADE, to='counter.Hash'),
            preserve_default=False,
        ),
    ]