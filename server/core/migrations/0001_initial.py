# Generated by Django 3.2.6 on 2021-08-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funciton', models.CharField(max_length=128)),
                ('dt', models.FloatField()),
                ('interval', models.FloatField()),
            ],
        ),
    ]