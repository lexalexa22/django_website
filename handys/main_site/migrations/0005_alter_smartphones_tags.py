# Generated by Django 3.2.19 on 2023-05-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_smartphones_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphones',
            name='tags',
            field=models.CharField(default=list, max_length=1000),
        ),
    ]