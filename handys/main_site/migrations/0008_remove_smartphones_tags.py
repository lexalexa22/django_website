# Generated by Django 3.2.19 on 2023-05-29 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_alter_smartphones_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphones',
            name='tags',
        ),
    ]
