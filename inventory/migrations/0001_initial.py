# Generated by Django 3.2 on 2022-10-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('stock', models.IntegerField()),
                ('availability', models.BooleanField()),
            ],
        ),
    ]