# Generated by Django 2.2.27 on 2022-03-15 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0060_auto_20220314_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='workstatus',
            field=models.IntegerField(choices=[(0, ''), (1, ''), (2, '')], default=0, verbose_name='資料狀態'),
        ),
        migrations.AlterField(
            model_name='log',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]