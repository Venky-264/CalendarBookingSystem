# Generated by Django 3.2.20 on 2023-09-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smail', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
                ('cname', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
            ],
        ),
    ]