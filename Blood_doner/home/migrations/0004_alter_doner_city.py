# Generated by Django 4.2.4 on 2023-09-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_doner_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doner',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
