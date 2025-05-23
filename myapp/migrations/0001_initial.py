# Generated by Django 4.2.20 on 2025-03-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('publishedYear', models.DateField()),
                ('availale', models.BooleanField(default=True)),
            ],
        ),
    ]
