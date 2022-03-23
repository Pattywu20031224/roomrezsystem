# Generated by Django 2.2.27 on 2022-03-23 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20220308_2055'),
        ('log', '0002_auto_20220316_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='classes',
            field=models.ForeignKey(default=305, on_delete=django.db.models.deletion.CASCADE, to='classes.Classes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='log',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
