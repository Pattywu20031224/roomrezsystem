# Generated by Django 2.2.27 on 2022-03-12 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0007_auto_20220312_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
