# Generated by Django 2.2.27 on 2022-03-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20220314_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='preface',
            field=models.ImageField(upload_to='', verbose_name='教室圖片'),
        ),
    ]
