# Generated by Django 2.2 on 2020-05-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0006_auto_20200510_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
