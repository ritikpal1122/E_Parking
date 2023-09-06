# Generated by Django 4.2 on 2023-04-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('ContactNo', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('UserName', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Gender', models.IntegerField(max_length=10)),
                ('Status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'signup',
            },
        ),
    ]
