# Generated by Django 4.2.2 on 2023-07-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductLinkHubApp', '0011_alter_product_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategorias',
            name='url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]
