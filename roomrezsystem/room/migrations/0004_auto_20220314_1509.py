# Generated by Django 2.2.27 on 2022-03-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room_preface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='preface',
            field=models.ImageField(blank=True, upload_to='', verbose_name='教室圖片'),
        ),
    ]
