# Generated by Django 4.1.3 on 2022-12-13 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_mhs_remove_devi_judul_delete_about_delete_devi'),
    ]

    operations = [
        migrations.CreateModel(
            name='th',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.mhs')),
            ],
        ),
    ]