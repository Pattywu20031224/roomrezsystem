# Generated by Django 2.2.27 on 2022-03-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20220308_2055'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classes',
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(to='classes.Classes'),
        ),
    ]