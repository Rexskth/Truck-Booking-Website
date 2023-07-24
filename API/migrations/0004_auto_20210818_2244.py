# Generated by Django 3.1.2 on 2021-08-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20210818_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='otpcontact',
            name='Email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='otpcontact',
            name='OTP',
            field=models.CharField(max_length=6),
        ),
    ]
