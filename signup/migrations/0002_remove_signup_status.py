# Generated by Django 4.2 on 2023-04-30 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='Status',
        ),
    ]
