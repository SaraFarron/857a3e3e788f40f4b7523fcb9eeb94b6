# Generated by Django 3.2.6 on 2021-08-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_function_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='graph',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/', verbose_name='График'),
        ),
    ]