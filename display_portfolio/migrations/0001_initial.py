# Generated by Django 4.1.3 on 2023-01-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_degree', models.CharField(max_length=15)),
                ('start_of_degree', models.DateField()),
                ('end_of_degree', models.DateField()),
                ('degree_city', models.CharField(max_length=15)),
                ('degree_country', models.TextField(max_length=15)),
            ],
        ),
    ]
