# Generated by Django 4.2.2 on 2023-07-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductLinkHubApp', '0014_imagenfondo_enlace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenfondo',
            name='imagen',
            field=models.ImageField(upload_to='ProductoLinkHubApp/imagenes_fondo'),
        ),
    ]
