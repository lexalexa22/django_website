# Generated by Django 3.2.19 on 2023-05-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphones',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
