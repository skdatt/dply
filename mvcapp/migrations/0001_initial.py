# Generated by Django 3.2.14 on 2022-08-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Dept', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Student Master',
            },
        ),
    ]