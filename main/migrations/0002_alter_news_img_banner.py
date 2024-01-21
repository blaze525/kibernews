# Generated by Django 5.0.1 on 2024-01-21 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, upload_to='news/'),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='banners/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.news')),
            ],
            options={
                'verbose_name': 'banners',
                'verbose_name_plural': 'banners',
                'db_table': 'banners',
            },
        ),
    ]
