# Generated by Django 4.0.6 on 2022-07-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
