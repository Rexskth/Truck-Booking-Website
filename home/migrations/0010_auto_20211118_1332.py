# Generated by Django 3.1.2 on 2021-11-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20211117_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrate',
            name='Rate',
            field=models.IntegerField(max_length=100),
        ),
    ]
