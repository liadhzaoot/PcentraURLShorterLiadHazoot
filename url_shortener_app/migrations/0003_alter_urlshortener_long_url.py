# Generated by Django 4.0.1 on 2022-01-29 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0002_alter_urlshortener_click_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='long_url',
            field=models.URLField(default=''),
        ),
    ]
