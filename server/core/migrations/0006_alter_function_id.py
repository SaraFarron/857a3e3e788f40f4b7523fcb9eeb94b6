# Generated by Django 3.2.6 on 2021-08-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_function_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]