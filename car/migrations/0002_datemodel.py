# Generated by Django 5.1.5 on 2025-01-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'date',
                'verbose_name_plural': 'dates',
            },
        ),
    ]
