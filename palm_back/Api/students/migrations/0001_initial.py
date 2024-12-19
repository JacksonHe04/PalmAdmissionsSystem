# Generated by Django 5.1.4 on 2024-12-15 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mytable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('graduationYear', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('birthDate', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('majorCount', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('percentage', models.CharField(max_length=20)),
                ('masterUniversity', models.CharField(max_length=255)),
                ('masterMajor', models.CharField(max_length=255)),
                ('tutor', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=255)),
                ('applicationType', models.CharField(max_length=50)),
                ('firstChoice', models.CharField(max_length=255)),
                ('secondChoice', models.CharField(max_length=255)),
                ('thirdChoice', models.CharField(max_length=255)),
                ('isAdjustable', models.BooleanField()),
                ('resume', models.TextField()),
                ('proofs', models.TextField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLeader', models.BooleanField()),
                ('awardTime', models.CharField(max_length=20)),
                ('awardName', models.CharField(max_length=255)),
                ('levelRanking', models.CharField(max_length=50)),
                ('mytable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='students.mytable')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicationTime', models.CharField(max_length=20)),
                ('journalConference', models.CharField(max_length=255)),
                ('paperName', models.CharField(max_length=255)),
                ('ccfLevel', models.CharField(max_length=10)),
                ('awardCategory', models.CharField(max_length=50)),
                ('mytable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='papers', to='students.mytable')),
            ],
        ),
    ]