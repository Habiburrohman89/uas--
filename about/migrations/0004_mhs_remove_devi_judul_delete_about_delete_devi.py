# Generated by Django 4.1.3 on 2022-12-12 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_devi'),
    ]

    operations = [
        migrations.CreateModel(
            name='mhs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.CharField(max_length=30)),
                ('NPM', models.CharField(max_length=20)),
                ('Prodi', models.CharField(max_length=30)),
                ('Tanggal_lahir', models.DateField()),
                ('Alamat', models.TextField()),
                ('Kode_pos', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='devi',
            name='judul',
        ),
        migrations.DeleteModel(
            name='about',
        ),
        migrations.DeleteModel(
            name='devi',
        ),
    ]
