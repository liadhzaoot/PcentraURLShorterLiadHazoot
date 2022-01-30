# Generated by Django 4.0.1 on 2022-01-29 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0003_alter_urlshortener_long_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortener',
            name='click_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='urlshortener',
            name='long_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='urlshortener',
            name='short_url',
            field=models.CharField(blank=True, default='', max_length=15, unique=True),
        ),
    ]
