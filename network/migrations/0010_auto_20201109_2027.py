# Generated by Django 3.1 on 2020-11-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]