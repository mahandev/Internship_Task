# Generated by Django 4.2.3 on 2023-07-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('price', models.IntegerField(max_length=5000)),
                ('shop', models.CharField(max_length=2000)),
                ('shop_rating', models.CharField(max_length=3)),
            ],
        ),
    ]