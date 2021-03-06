# Generated by Django 2.2 on 2020-06-18 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showInfo', '0008_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Female',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Male',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='M2F',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fmale', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='showInfo.Female')),
                ('male', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='showInfo.Male')),
            ],
        ),
    ]
