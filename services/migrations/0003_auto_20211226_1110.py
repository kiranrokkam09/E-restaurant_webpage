# Generated by Django 3.2.7 on 2021-12-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20211226_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebooking',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='time',
            field=models.TimeField(),
        ),
    ]