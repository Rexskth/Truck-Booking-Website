# Generated by Django 3.1.2 on 2021-08-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20210811_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='otpcontact',
            name='Name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='otpcontact',
            name='OTP',
            field=models.EmailField(max_length=254),
        ),
    ]