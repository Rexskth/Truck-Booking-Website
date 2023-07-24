# Generated by Django 3.1.2 on 2021-03-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A_business', '0002_auto_20210323_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser_abusniess',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='extendeduser_abusniess',
            name='Longitude',
        ),
        migrations.RemoveField(
            model_name='extendeduser_abusniess',
            name='Speed',
        ),
        migrations.RemoveField(
            model_name='extendeduser_abusniess',
            name='timeStamp',
        ),
        migrations.AddField(
            model_name='extendeduser_abusniess',
            name='signup_email',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='extendeduser_abusniess',
            name='signup_phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='extendeduser_abusniess',
            name='signup_username',
            field=models.CharField(default='', max_length=15),
        ),
    ]
