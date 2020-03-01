# Generated by Django 3.0.3 on 2020-02-29 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier_announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=300)),
                ('paragraph1', models.TextField(blank=True)),
                ('paragraph2', models.TextField(blank=True)),
                ('paragraph3', models.TextField(blank=True)),
                ('paragraph4', models.TextField(blank=True)),
                ('paragraph5', models.TextField(blank=True)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('posted_by', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(default=True)),
                ('picture1', models.ImageField(blank=True, upload_to='photos/carrier/%Y/%m/%d/')),
                ('picture2', models.ImageField(blank=True, upload_to='photos/carrier/%Y/%m/%d/')),
                ('file1', models.FileField(blank=True, upload_to='files/carrier/%Y/%m/%d/')),
                ('file2', models.FileField(blank=True, upload_to='files/carrier/%Y/%m/%d/')),
                ('file3', models.FileField(blank=True, upload_to='files/carrier/%Y/%m/%d/')),
                ('file4', models.FileField(blank=True, upload_to='files/carrier/%Y/%m/%d/')),
            ],
        ),
    ]