# Generated by Django 2.0.1 on 2018-01-27 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicMessage', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('establishedOn', models.DateTimeField()),
                ('totalAmountDonated', models.FloatField(default=0)),
                ('iconID', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('fullName', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('aboutMe', models.CharField(max_length=200)),
                ('birthdate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iconID', models.IntegerField(default=1)),
                ('totalAmountDonated', models.FloatField(default=0)),
                ('maximumAmount', models.FloatField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('charity', models.CharField(max_length=200)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charitown.Community')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalAMountDonated', models.FloatField(default=0)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charitown.Member')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charitown.Project')),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='member',
            field=models.ManyToManyField(to='charitown.Member'),
        ),
    ]
