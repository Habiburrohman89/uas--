# Generated by Django 4.1.3 on 2022-11-17 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('komen', models.CharField(max_length=200)),
            ],
        ),
    ]
