# Generated by Django 2.2.5 on 2021-05-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0008_auto_20210522_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='palmapplicant',
            name='submit_time',
            field=models.CharField(default='0', max_length=100, verbose_name='提交时间'),
        ),
    ]