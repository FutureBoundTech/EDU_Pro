# Generated by Django 5.1.1 on 2025-03-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='')),
                ('d_img', models.ImageField(upload_to='')),
                ('info', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
