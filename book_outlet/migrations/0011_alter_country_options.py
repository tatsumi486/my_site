# Generated by Django 4.1.4 on 2022-12-30 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0010_country_alter_address_options_book_published_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]