# Generated by Django 3.2.7 on 2021-12-26 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_tablebooking_person2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablebooking',
            name='person',
        ),
        migrations.DeleteModel(
            name='costumer',
        ),
    ]
