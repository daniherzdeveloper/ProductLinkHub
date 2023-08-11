# Generated by Django 4.2.2 on 2023-08-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductLinkHubApp', '0019_remove_subcategorias_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubCategoriaSeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField()),
                ('disponible', models.BooleanField(default=True)),
                ('subcategoria_seccion', models.ManyToManyField(to='ProductLinkHubApp.subcategoriaseccion')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]