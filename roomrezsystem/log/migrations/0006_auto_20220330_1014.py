# Generated by Django 2.2.27 on 2022-03-30 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_merge_20220326_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
