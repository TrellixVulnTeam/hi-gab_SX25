# Generated by Django 2.0.1 on 2018-01-27 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charitown', '0002_member_totalamountdonated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='member',
            new_name='members',
        ),
    ]