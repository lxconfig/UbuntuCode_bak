# Generated by Django 3.1.3 on 2020-11-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('token', models.CharField(blank=True, max_length=64, null=True, verbose_name='用户口令')),
            ],
        ),
    ]
