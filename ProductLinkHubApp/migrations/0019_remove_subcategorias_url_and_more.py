# Generated by Django 4.2.2 on 2023-08-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductLinkHubApp', '0018_subcategoriaseccion_url_texto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategorias',
            name='url',
        ),
        migrations.RemoveField(
            model_name='subcategoriaseccion',
            name='url',
        ),
        migrations.AddField(
            model_name='subcategorias',
            name='url_texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]
