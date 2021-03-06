# Generated by Django 3.0.3 on 2020-02-26 04:55

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('id_or_passport', models.CharField(blank=True, max_length=50)),
                ('location_in_Korea', models.CharField(blank=True, max_length=100)),
                ('institution', models.CharField(blank=True, max_length=100)),
                ('education_level', models.CharField(blank=True, max_length=50)),
                ('major_or_field_of_work', models.CharField(blank=True, max_length=100)),
                ('graduation_year', models.DateField(blank=True)),
                ('activity', models.CharField(blank=True, max_length=50)),
                ('other_information', models.TextField(blank=True)),
            ],
        ),
    ]
