# Generated by Django 2.2.27 on 2022-03-12 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0014_auto_20220312_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
