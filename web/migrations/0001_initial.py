# Generated by Django 5.1.5 on 2025-01-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('ad_num', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
