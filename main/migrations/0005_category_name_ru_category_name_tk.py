# Generated by Django 5.0.1 on 2024-01-26 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_tk',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
    ]