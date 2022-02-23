# Generated by Django 3.1.4 on 2022-02-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=48, verbose_name='教室名稱')),
                ('detail', models.TextField(blank=True, verbose_name='詳細資訊')),
                ('status', models.IntegerField(choices=[(0, '使用中'), (1, '開放使用')], default=0, verbose_name='狀態')),
            ],
        ),
    ]